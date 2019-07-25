# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['sphinx_gherkindoc']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=1.3',
 'behave>=1.2.6',
 'recommonmark>=0.4.0',
 'sphinx_rtd_theme>=0.3.1']

entry_points = \
{'console_scripts': ['sphinx-gherkinconfig = sphinx_gherkindoc.cli:config',
                     'sphinx-gherkindoc = sphinx_gherkindoc.cli:main']}

setup_kwargs = {
    'name': 'sphinx-gherkindoc',
    'version': '3.2.5',
    'description': 'A tool to convert Gherkin into Sphinx documentation',
    'long_description': 'sphinx-gherkindoc\n=================\n\n``sphinx-gherkindoc`` brings Gherkin goodness\ninto the Sphinx/reStructuredText (rST) world.\n\nWhy should I use it?\n--------------------\n\n**Share your requirements with your larger team.**\nGherkin makes it easy for anyone to read requirements.\nSphinx makes Gherkin pretty enough to be readable.\n``sphinx-gherkindoc`` handles converting flat-text feature files\ninto easy to read documents you won\'t cringe to share with your larger team.\n\n**Easily see what steps you have and where you are using them.**\n``sphinx-gherkindoc`` can create a glossary of your steps.\nThis helps makes it easy to:\n\n   * find steps to reuse\n   * notice similar steps that might be duplicates or unintended variations\n   * see patterns that you might exploit to reduce the number of steps you have\n   * find out where and which feature files would be affected\n     if a step\'s wording or implementation changes\n\n\nHow does it do that?\n--------------------\n\n``sphinx-gherkindoc`` recursively scans a given directory\nto find all the feature and markup files,\nand converts them into files\nthat can be included in Sphinx-based documentation.\nThis script was inspired by ``sphinx-apidoc``\nwhich does a similar thing for source code.\n\n.. Note::\n\n    This tool only creates the rST inputs for a sphinx document run,\n    you still need to fit these files\n    in to your larger documentation building process yourself.\n\nFor specific details on the command line options,\nplease consult the ``--help`` output.\nMost command line options mirror their counterpart in ``sphinx-apidoc``.\n\nFor the most basic usage, an input (``<gherkin_path>``)\nand output (``<output_path>``) path must be provided.\nThe files put in to the ``<output_path>``\ncan be incorporated into any larger documentation,\ncreated by any means.\n\nAdditionally, a list of ``fnmatch``-compatible patterns can be added\nto the command line,\nto indicate directories to be excluded from processing.\n\nOne notable addition is the step glossary(``-G``, ``--step-glossary``).\nThe step glossary command line option causes ``sphinx-gherkindoc``\nto create the named file in the ``<output_path>`` directory.\nThe step glossary content is formatted into two lists:\n\n   * A list of all the steps found, in alphabetical order.\n     Each item in this list is a link to its details in the second list.\n   * A list of the steps showing the file names and line numbers\n     where they are used.\n     This list is in order by the most number of uses first.\n\n\nHow are my files converted?\n---------------------------\n\nWhen scanning the ``<gherkin_path>`` directory tree,\n``sphinx-gherkindoc`` will do the following:\n\n   * Feature files found\n     are processed into rST files in the ``<output_path>`` directory.\n   * Directories will be converted to Sphinx Table of Contents (TOC) files that\n     link to any feature files in the same directory,\n     and to any TOC files from direct subdirectories.\n   * Any rST files found in a directory have their contents copied\n     to the front of the TOC file for that directory.\n     If more than one rST file is found in a directory,\n     they are processed in sort order.\n   * If no rST files are found in a directory,\n     then a header for the TOC is created based\n     on the contents of a ``display_name.txt`` file, if present,\n     or the name of the directory.\n   * Any MarkDown (md) files are referenced\n     from the TOC file for the directory they are in.\n   * Directories with no feature, rST, or md files are pruned,\n     recursively upwards.\n\n\nThe meat\'n\'potatoes will be your feature files.\nPut rST files next to your feature files\nto present context and additional helpful material.\nIf any rST files are in the same directory,\nthey should also contain any appropriate headers\nand other such formatting.\n``sphinx-gherkindoc`` will only create (minimal) headers when\nthere are no rST files present at all.\n\n\nExamples\n--------\n\nDisclaimer: This `is not` a tutorial on how to use or configure Sphinx.\nIt `is` some common ways you can use ``sphinx-gherkindoc``\nas part of your documentation generation.\nReminder if you skipped all that stuff above:\n``--help`` will show you the default values\nwhen command line options aren\'t used.\n\nConventions - Sphinx-based document production usually uses two directories:\n\n    * ``_docs`` - the working directory where we put all the rST files\n      from the various tools as we are building documents.\n      This directory shoud not be checked in to version control\n      and should only contain files created by a documentation run.\n    * ``docs`` - the output directory for a documentation run.\n      For example, this is where ``index.html`` is found\n      when building HTML docs, etc.\n      This directory should not be checked in to version control\n      as it contains only derived and processed files.\n\n\n1. Convert feature files to rST;\n   process all feature and document files\n   in/under ``feature/root/directory-here`` into the ``_docs`` directory\n   using all the defaults::\n\n       sphinx-gherkindoc feature/root/directory-here _docs\n\n2. Same as above,\n   but also create a step glossary file ``my_step_glossary`` in ``_docs``::\n\n       sphinx-gherkindoc -G my_step_glossary feature/root/directory-here _docs\n\n3. Experiment!\nOnce you have the 2nd step working\nand integrated in to your document building process,\nyou may find you want to tweak the results some.\nIt\'s a lot easier to do that `after` you have the basic process working.\nExperiment with the other optional parameters\nto get the effect(s) you want.\n\nSpecial Instructions for Tag Links\n----------------------------------\n\nAny tag can be converted into an anonymous link\nvia a plugin or command-line argument.\nThe converter needs to be a single function\nthat accepts a single string parameter, the tag,\nand returns a URL if the tag should include a link\nor an empty string if not.\n\nIn order to register the plugin for a ``poetry``-based project::\n\n    [tools.poetry.plugins."parsers"]\n    url = "my_custom_library.parse:optional_url_from_tag"\n\nIn order to register the plugin for a ``setup.py``-based project::\n\n    setup(\n        ...\n        entry_points={\n            \'parsers\': [\'url = my_custom_library.parse:optional_url_from_tag\']\n        }\n    )\n\nIn order to use the parser via command line,\nthe ``--url_from-tag`` flag should be used.\nThe provided string should be be formatted ``<library>:<method_name>``\n',
    'author': 'Lewis Franklin',
    'author_email': 'lewis.franklin@gmail.com',
    'url': 'https://jolly-good-toolbelt.github.io/sphinx_gherkindoc/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
