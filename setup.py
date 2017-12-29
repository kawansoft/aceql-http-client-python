from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='aceql',
    version='1.0.2',
    packages=['aceql', 'aceql._private', 'tests'],
    url='https://github.com/kawansoft/aceql-py',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    keywords='SQL HTTP',
    install_requires=[
        'requests>=2.18.4',
        'requests_toolbelt>=0.8.0',
        'pytz>=2017.3'
    ],

    package_data={
        # If any package contains *.txt or *.png or s*.rst files, include them:
        '': ['*.txt', '*.png', '*.rst']
    },

    author='KawanSoft',
    author_email='contact@kawansoft.com',
    description='Python 2 & 3 Client toolkit for easy access of remote SQL databases managed with AceQL HTTP.'
)
