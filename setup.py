import os
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return Path(os.path.join(os.path.dirname(__file__), *rnames)).read_text()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('src', 'zc', 'zodbrecipes', 'zeo.txt')
    + '\n' +
    'Download\n'
    '**********************\n'
)

name = "zc.zodbrecipes"
setup(
    name=name,
    version='3.2.dev0',
    author="Jim Fulton",
    author_email="zope-dev@zope.dev",
    description="ZC Buildout recipes for ZODB",
    license="ZPL-2.1",
    keywords="zodb buildout",
    url='https://github.com/zopefoundation/zc.zodbrecipes',
    long_description=long_description,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['zc'],
    python_requires='>=3.9',
    install_requires=[
        'zc.buildout',
        'setuptools',
        'zc.recipe.egg',
        'ZConfig >=2.4'
    ],
    extras_require=dict(test=[
        'zdaemon',
        'ZEO',
        'zope.event',
        'zope.testing',
        'zope.proxy',
        'zope.testrunner',
        'zodbpickle',
    ]),
    entry_points={
        'zc.buildout': [
            'server = %s:StorageServer' % name,
        ]
    },
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
