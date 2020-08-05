import os
import re
from setuptools import setup

about = {}
with open('flask_cognito/__about__.py') as f:
    exec(f.read(), about)

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')) as f:
    test_required = f.read().splitlines()

setup(
    name='SB Flask Cognito',
    version='0.1',
    url='https://github.com/ScriptonBasestar-io/sb-flask-cognito',
    license='MIT',
    author='CE',
    author_email='archmagece@gmail.com',
    description='',
    long_description=README,
    long_description_content_type='text/markdown'
    # packages=['sb_flask_cognito'],
    py_modules=['sb_flask_cognito'],
    zip_safe=False,
    include_package_data=True,
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='flask aws cognito jwt authentication auth serverless async',
)
