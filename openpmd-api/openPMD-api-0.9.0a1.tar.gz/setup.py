import os
import re
import sys
import platform
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake 3.11.0+ must be installed to build the following " +
                "extensions: " +
                ", ".join(e.name for e in self.extensions))

        cmake_version = LooseVersion(re.search(
            r'version\s*([\d.]+)',
            out.decode()
        ).group(1))
        if cmake_version < '3.11.0':
            raise RuntimeError("CMake >= 3.11.0 is required")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)
        ))
        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
            '-DCMAKE_PYTHON_OUTPUT_DIRECTORY=' + extdir,
            '-DPYTHON_EXECUTABLE=' + sys.executable,
            # variants
            '-DopenPMD_USE_MPI:BOOL=' + openPMD_USE_MPI,
            # skip building tests & examples
            '-DBUILD_TESTING:BOOL=' + BUILD_TESTING,
            '-DBUILD_EXAMPLES:BOOL=' + BUILD_EXAMPLES,
            # static/shared libs
            '-DBUILD_SHARED_LIBS:BOOL=' + BUILD_SHARED_LIBS,
            '-DHDF5_USE_STATIC_LIBRARIES:BOOL=' + HDF5_USE_STATIC_LIBRARIES,
            '-DADIOS_USE_STATIC_LIBS:BOOL=' + ADIOS_USE_STATIC_LIBS,
            # Unix: rpath to current dir when packaged
            '-DCMAKE_INSTALL_RPATH=$ORIGIN',
            '-DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON',
            '-DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=OFF',
            # Windows: will already have %PATH% in package dir
        ]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += [
                '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(
                    cfg.upper(),
                    extdir
                )
            ]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j2']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get('CXXFLAGS', ''),
            self.distribution.get_version()
        )
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(
            ['cmake', ext.sourcedir] + cmake_args,
            cwd=self.build_temp,
            env=env
        )
        subprocess.check_call(
            ['cmake', '--build', '.'] + build_args,
            cwd=self.build_temp
        )


with open('./README.md', encoding='utf-8') as f:
    long_description = f.read()

# Allow to control options via environment vars.
# Work-around for https://github.com/pypa/setuptools/issues/1712
# note: changed default for MPI, TESTING and EXAMPLES
openPMD_USE_MPI = os.environ.get('openPMD_USE_MPI', 'OFF')
HDF5_USE_STATIC_LIBRARIES = os.environ.get('HDF5_USE_STATIC_LIBRARIES', 'OFF')
ADIOS_USE_STATIC_LIBS = os.environ.get('ADIOS_USE_STATIC_LIBS', 'OFF')
BUILD_SHARED_LIBS = os.environ.get('BUILD_SHARED_LIBS', 'ON')
BUILD_TESTING = os.environ.get('BUILD_TESTING', 'OFF')
BUILD_EXAMPLES = os.environ.get('BUILD_EXAMPLES', 'OFF')

# https://cmake.org/cmake/help/v3.0/command/if.html
if openPMD_USE_MPI.upper() in ['1', 'ON', 'YES', 'TRUE', 'YES']:
    openPMD_USE_MPI = "ON"
else:
    openPMD_USE_MPI = "OFF"

# Get the package requirements from the requirements.txt file
with open('./requirements.txt') as f:
    install_requires = [line.strip('\n') for line in f.readlines()]
    if openPMD_USE_MPI == "ON":
        install_requires.append('mpi4py>=2.1.0')

# keyword reference:
#   https://packaging.python.org/guides/distributing-packages-using-setuptools
setup(
    name='openPMD-api',
    # note PEP-440 syntax: x.y.zaN but x.y.z.devN
    version='0.9.0a1',
    author='Fabian Koller, Franz Poeschel, Axel Huebl',
    author_email='f.koller@hzdr.de, f.poeschel@hzdr.de, a.huebl@hzdr.de',
    maintainer='Axel Huebl',
    maintainer_email='a.huebl@hzdr.de',
    description='C++ & Python API for Scientific I/O with openPMD',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=('openPMD openscience hdf5 adios mpi hpc research '
              'file-format file-handling'),
    url='https://www.openPMD.org',
    project_urls={
        'Documentation': 'https://openpmd-api.readthedocs.io',
        'Doxygen': 'https://www.openpmd.org/openPMD-api',
        'Reference': 'https://doi.org/10.14278/rodare.27',
        'Source': 'https://github.com/openPMD/openPMD-api',
        'Tracker': 'https://github.com/openPMD/openPMD-api/issues',
    },
    ext_modules=[CMakeExtension('openpmd_api')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
    python_requires='>=3.5, <3.8',
    # tests_require=['pytest'],
    install_requires=install_requires,
    # we would like to use this mechanism, but pip / setuptools do not
    # influence the build and build_ext with it.
    # therefore, we use environment vars to control.
    # ref: https://github.com/pypa/setuptools/issues/1712
    # extras_require={
    #     'mpi': ['mpi4py>=2.1.0'],
    # },
    # cmdclass={'test': PyTest},
    # platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Database :: Front-Ends',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ('License :: OSI Approved :: '
         'GNU Lesser General Public License v3 or later (LGPLv3+)'),
    ],
)
