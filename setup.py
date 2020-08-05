'''
Flask-AWSCognito
-------------

User authentication with AWS Cognito for Flask
'''
from setuptools import setup, find_packages
import os

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
    name='SB Flask AWSCognito',
    version='0.1',
    url='https://github.com/ScriptonBasestar-io/sb-flask-cognito',
    license='MIT',
    author='CE',
    author_email='archmagece@gmail.com',
    description='이것저것합쳐서',
    long_description=README,
    long_description_content_type='text/markdown',
    py_modules=['flask_cognito'],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[required, 'Flask', 'python-jose', 'requests'],
    tests_require=[test_required],
    extras_require={'tests': test_required},
    python_requires='>=3.6',
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