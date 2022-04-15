from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aceql',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='5.4',
    packages=['aceql', 'aceql._private', 'aceql._private.batch', 'aceql._private.dto','aceql.metadata'],
    url='https://github.com/kawansoft/aceql-py',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    keywords='DATABASE SQL HTTP CLIENT-SERVER',
    install_requires=[
        'requests>=2.18.4,<3.0.0',
        'requests_toolbelt>=0.8.0',
        'pytz>=2017.3',
        'marshmallow',
        'ijson'
    ],

    package_data={
        # If any package contains *.txt or *.png or s*.rst files, include them:
        '': ['*.txt', '*.png', '*.md', '*.rst']
    },

    author='KawanSoft',
    author_email='contact@kawansoft.com',
    description='Python 3 Client toolkit for easy access of remote SQL databases managed with AceQL HTTP.'
)
