from setuptools import setup

setup(
    name='aceql',
    version='1.0.0',
    packages=['aceql', 'aceql._private', 'tests'],
    url='https://github.com/kawansoft/aceql-py',
    license='Apache 2.0',

    install_requires=[
        'requests>=2.18.4',
        'requests_toolbelt>=0.8.0',
        'pytz>=2017.3'
    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.png', '*.rst']
    },

    author='KawanSoft',
    author_email='contact@kawansoft.com',
    description='Python 2 & 3 Client toolkit for easy access of remote SQL databases managed with AceQL HTTP.'
)
