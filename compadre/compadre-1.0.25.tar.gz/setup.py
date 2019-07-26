import os
import sys
import distutils

import subprocess 
import shutil

import pkg_resources
# rather than deal with --no-build-isolation flags and other various flags to get a decent CMake build,
# we do not use build and install requirements in pyproject.toml

min_wheel_version = ['0','33','1']
min_numpy_version = ['1','16','0']
min_cmake_version = ['3','0','0']

min_wheel_version_str = '.'.join(min_wheel_version)
min_numpy_version_str = '.'.join(min_numpy_version)
min_cmake_version_str = '.'.join(min_cmake_version)

is_error = False
error_msg = ""

try:
    import pathlib2
except ImportError:
    is_error = True
    error_msg = error_msg + """You need the Python 'pathlib2' package!
        install it by running 'pip install pathlib2'""" + "\n"

try:
    import wheel
    wheel_version = pkg_resources.get_distribution("wheel").version.split('.')
    assert wheel_version >= min_wheel_version
except ImportError:
    is_error = True
    error_msg = error_msg + """You need the Python 'wheel' package >= %s!
        install it by running 'pip install wheel'"""%(min_wheel_version_str,) + "\n"

try:
    import numpy
    numpy_version = pkg_resources.get_distribution("numpy").version.split('.')
    assert numpy_version >= min_numpy_version
except ImportError:
    is_error = True
    error_msg = error_msg + """You need the Python 'numpy' package >= %s!
        install it by running 'pip install numpy'"""%(min_numpy_version_str,) + "\n"

try:
    import cmake
    cmake_version = pkg_resources.get_distribution("cmake").version.split('.')
    assert cmake_version >= min_cmake_version
except ImportError:
    is_error = True
    error_msg = error_msg + """You need the Python 'cmake' package >= %s!
        install it by running 'pip install cmake'"""%(min_cmake_version_str,) + "\n"

if is_error:
    sys.exit(error_msg)

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig
from setuptools.command.install import install

#inspired by pieces from
#https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
#https://martinopilia.com/posts/2018/09/15/building-python-extension.html
#https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools
#https://stackoverflow.com/questions/18725137/how-to-obtain-arguments-passed-to-setup-py-from-pip-with-install-option

def is_osx():
    name = distutils.util.get_platform()
    if sys.platform != 'darwin':
        return False
    elif name.startswith('macosx-10'):
        minor_version = int(name.split('-')[1].split('.')[1])
        if minor_version >= 7:
            return True
        else:
            return False
    else:
        return False

class CMakeExtension(Extension):
    def __init__(self, name, cmake_lists_dir='.', **kwa):
        Extension.__init__(self, name, sources=[], **kwa)
        self.cmake_lists_dir = os.path.abspath(cmake_lists_dir)

class InstallCommand(install):
    user_options = install.user_options + [
        ('use-gpu', None, None),
        ('use-openmp', None, None),
        ('disable-openmp', None, None),
        ('use-pthread', None, None),
        ('disable-pthread', None, None),
        ('kokkos-arch=', None, None),
        ('trilinos-prefix=', None, None),
        ('kokkos-prefix=', None, None),
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.use_gpu = None
        self.use_openmp = None
        self.disable_openmp = None
        self.use_pthread = None
        self.disable_pthread = None
        self.kokkos_arch = None
        self.trilinos_prefix = None
        self.kokkos_prefix = None

    def finalize_options(self):
        print("--use-gpu:", self.use_gpu)
        print("--use-openmp:", self.use_openmp)
        print("--disable-openmp:", self.disable_openmp)
        print("--use-pthread:", self.use_pthread)
        print("--disable-pthread:", self.disable_pthread)
        print("--kokkos-arch:", self.kokkos_arch)
        print("--trilinos-prefix:", self.kokkos_arch)
        print("--kokkos-prefix:", self.kokkos_arch)
        install.finalize_options(self)

    def run(self):

        global use_gpu
        global use_openmp
        global disable_openmp
        global use_pthread
        global disable_pthread
        global kokkos_arch
        global trilinos_prefix
        global kokkos_prefix

        use_gpu = self.use_gpu
        use_openmp = self.use_openmp
        disable_openmp = self.disable_openmp
        use_pthread = self.use_pthread
        disable_pthread = self.disable_pthread
        kokkos_arch = self.kokkos_arch
        trilinos_prefix = self.trilinos_prefix
        kokkos_prefix = self.kokkos_prefix
        install.run(self)

class build_ext(build_ext_orig):

    def run(self):
        for ext in self.extensions:
            self.build_cmake(ext)
        build_ext_orig.run(self)


    def build_cmake(self, ext):

        # Accepts user provided compile, link, and python linker specific flags
        COMPILE_OPTIONS = []
        LINK_OPTIONS = []
        PYTHON_SPECIFIC_LINK_OPTIONS = []
        
        if is_osx():
            COMPILE_OPTIONS.append("-stdlib=libc++")
            LINK_OPTIONS.append("-lc++")
            PYTHON_SPECIFIC_LINK_OPTIONS.append("-undefined dynamic_lookup -nodefaultlibs")


        # Get location for where GMLS_Module will be installed
        cwd = pathlib2.Path().absolute()
        build_temp = pathlib2.Path(self.build_temp)
        try:
            build_temp.mkdir(parents=True)
        except:
            pass # already exists
        extdir = pathlib2.Path(self.get_ext_fullpath(ext.name))
        try:
            extdir.mkdir(parents=True)
        except:
            pass # already exists


        # Parse bool for using GPU
        use_gpu_string = "OFF"
        try:
            if use_gpu != None:
                use_gpu_string = "ON"
                print("Compadre_USE_CUDA set to ON")
            else:
                print("Compadre_USE_CUDA set to OFF")
        except:
            print("Compadre_USE_CUDA set to OFF")

        # Parse bool for using OpenMP
        use_openmp_string = ""
        # check if turned on
        try:
            if use_openmp != None:
                use_openmp_string = "ON"
                print("Compadre_USE_OpenMP set to ON")
            else:
                print("Compadre_USE_OpenMP not set by Python")
        except:
            print("Compadre_USE_OpenMP not set by Python")
        # check if turned off
        try:
            if disable_openmp != None:
                use_openmp_string = "OFF"
                print("Compadre_USE_OpenMP set to OFF")
            else:
                print("Compadre_USE_OpenMP not set by Python")
        except:
            print("Compadre_USE_OpenMP not set by Python")

        # Parse bool for using Pthread
        use_pthread_string = ""
        # check if turned on
        try:
            if use_pthread != None:
                use_pthread_string = "ON"
                print("Compadre_USE_Pthread set to ON")
            else:
                print("Compadre_USE_Pthread not set by Python")
        except:
            print("Compadre_USE_Pthread not set by Python")
        # check if turned off
        try:
            if disable_pthread != None:
                use_pthread_string = "OFF"
                print("Compadre_USE_Pthread set to OFF")
            else:
                print("Compadre_USE_Pthread not set by Python")
        except:
            print("Compadre_USE_Pthread not set by Python")

        # Parse string for kokkos architecture
        kokkos_arch_string = ""
        try:
            if kokkos_arch != None:
                kokkos_arch_string = str(kokkos_arch)
                print("KokkosCore_ARCH set to: %s"%(kokkos_arch_string,))
            else:
                print("KokkosCore_ARCH not set.")
        except:
            print("KokkosCore_ARCH not set.")

        # Parse string for trilinos prefix (containing a kokkos install, optional)
        trilinos_prefix_string = ""
        try:
            if trilinos_prefix != None:
                trilinos_prefix_string = str(trilinos_prefix)
                print("Trilinos_PREFIX set to: %s"%(trilinos_prefix_string,))
            else:
                print("Trilinos_PREFIX not set in Python.")
        except:
            print("Trilinos_PREFIX not set in Python.")

        # Parse string for kokkos prefix (user installed previous to python package install, optional)
        kokkos_prefix_string = ""
        try:
            if kokkos_prefix != None:
                kokkos_prefix_string = str(kokkos_prefix)
                print("KokkosCore_PREFIX set to: %s"%(kokkos_prefix_string,))
            else:
                print("KokkosCore_PREFIX not set in Python.")
        except:
            print("KokkosCore_PREFIX not set in Python.")


        # Configure CMake
        config = 'Debug' if self.debug else 'Release'
        cmake_args = [
            '-DGMLS_Module_DEST=' + str(extdir.parent.absolute()),
            '-DCMAKE_INSTALL_PREFIX=' + str(extdir.parent.absolute()),
            '-DCMAKE_CXX_FLAGS=' + " ".join(COMPILE_OPTIONS),
            '-DCMAKE_SHARED_LINKER_FLAGS=' + " ".join(LINK_OPTIONS),
            '-DCMAKE_PYTHON_SHARED_LINKER_FLAGS=' + " ".join(PYTHON_SPECIFIC_LINK_OPTIONS),
            '-DPYTHON_EXECUTABLE=' + str(sys.executable),
            '-DCMAKE_OSX_DEPLOYMENT_TARGET=10.11',
            '-DCompadre_USE_PYTHON:BOOL=ON',
            '-DCompadre_USE_MATLAB:BOOL=ON',
            '-DCompadre_EXAMPLES:BOOL=OFF',
            '-DPYTHON_CALLING_BUILD:BOOL=ON',
            '-DCompadre_USE_CUDA:BOOL=%s'%(use_gpu_string,),
            '-DCompadre_USE_OpenMP:BOOL=%s'%(use_openmp_string,),
            '-DCompadre_USE_Pthread:BOOL=%s'%(use_pthread_string,),
            '-DKokkosCore_ARCH:STRING=%s'%(kokkos_arch_string,),
        ]
        if kokkos_prefix_string != "":
            cmake_args.append('-DKokkosCore_PREFIX:STRING=%s'%(kokkos_prefix_string,))
        if trilinos_prefix_string != "":
            cmake_args.append('-DTrilinos_PREFIX:STRING=%s'%(trilinos_prefix_string,))
        else:
            cmake_args.append('-DCMAKE_BUILD_TYPE=' + config)
        build_args = [
            '--config', config,
            '--', '-j4'
        ]
        os.chdir(str(build_temp))
        self.spawn(['cmake', str(cwd)] + cmake_args)
        if not self.dry_run:
            self.spawn(['cmake', '--build', '.'] + build_args)

        # copy files from this build directory
        python_temp = "./python"
        dest_temp = "../" + extdir.relative_to(*extdir.parts[:1]).as_posix() + "/../compadre"
        libs = [os.path.join(python_temp, _lib) for _lib in 
                os.listdir(python_temp) if 
                os.path.isfile(os.path.join(python_temp, _lib)) and 
                os.path.splitext(_lib)[1] in [".dll", ".so", ".dylib",".py"]
                and not (_lib.startswith("python"))]
        for lib in libs:
            shutil.move(lib, os.path.join(dest_temp,
                                          os.path.basename(lib)))

        # copy files from this build directory
        python_temp = "./src"
        dest_temp = "../" + extdir.relative_to(*extdir.parts[:1]).as_posix() + "/../compadre"
        libs = [os.path.join(python_temp, _lib) for _lib in 
                os.listdir(python_temp) if 
                os.path.isfile(os.path.join(python_temp, _lib)) and 
                os.path.splitext(_lib)[1] in [".dll", ".so", ".dylib"]
                and not (_lib.startswith("python"))]
        for lib in libs:
            shutil.move(lib, os.path.join(dest_temp,
                                          os.path.basename(lib)))

        os.chdir(str(cwd))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="compadre",
    version="1.0.25", # generated by create_package.sh argument
    setup_requires=[
          "pathlib2",
          "wheel>=%s"%(min_wheel_version_str,),
          "numpy>=%s"%(min_numpy_version_str,),
          "cmake>=%s"%(min_cmake_version_str,),
    ],
    install_requires=[
          "numpy>=%s"%(min_numpy_version_str,),
    ],
    author="Paul Kuberry",
    author_email="pkuberry@gmail.com",
    description="Compatible Particle Discretization and Remap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SNLComputation/compadre",
    packages=['compadre'],
    package_dir={'compadre': 'python/compadre'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
    ],
    ext_modules=[CMakeExtension('compadre')],
    cmdclass={
        'build_ext': build_ext,
        'install': InstallCommand
    },
    include_package_data=False
)
