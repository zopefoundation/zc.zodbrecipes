import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('zc', 'zodbrecipes', 'zeo.txt')
    + '\n' +
    'Download\n'
    '**********************\n'
    )

open('doc.txt', 'w').write(long_description)

tests_require = [
    'zdaemon',
    'ZODB',
    'ZEO',
    'zope.testing',
    'zope.proxy',
    ]

name = "zc.zodbrecipes"
setup(
    name = name,
    version='0.6.3dev',
    author = "Jim Fulton",
    author_email = "jim@zope.com",
    description = "ZC Buildout recipes for ZODB",
    license = "ZPL 2.1",
    keywords = "zodb buildout",
    url='http://svn.zope.org/'+name,
    long_description=long_description,

    packages = find_packages('.'),
    include_package_data = True,
    namespace_packages = ['zc'],
    install_requires = ['zc.buildout', 'setuptools',
                        'zc.recipe.egg', 'ZConfig >=2.4'],
    extras_require = dict(test=tests_require),
    entry_points = {
        'zc.buildout': [
             'server = %s:StorageServer' % name,
             ]
         },
    classifiers = [
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    test_suite='zc.zodbrecipes.tests.test_suite',
    tests_require=tests_require,
    )
