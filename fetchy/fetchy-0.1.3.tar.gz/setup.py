# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['fetchy', 'fetchy.cli']

package_data = \
{'': ['*'], 'fetchy.cli': ['commands/*']}

install_requires = \
['PyInquirer>=1.0,<2.0',
 'cleo>=0.7.5,<0.8.0',
 'distro>=1.4,<2.0',
 'docker>=4.0,<5.0',
 'tqdm>=4.32,<5.0',
 'unix_ar>=0.2.1,<0.3.0',
 'validators>=0.13.0,<0.14.0']

entry_points = \
{'console_scripts': ['fetchy = fetchy.cli:main']}

setup_kwargs = {
    'name': 'fetchy',
    'version': '0.1.3',
    'description': 'Downloading packages made easy!',
    'long_description': None,
    'author': 'thomas',
    'author_email': 'thomas.kluiters@gmail.com',
    'url': 'https://github.com/ThomasKluiters/fetchy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
