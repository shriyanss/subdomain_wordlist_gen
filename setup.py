from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='subgen',
    version='0.0.1',
    author='Shriyans Sudhi',
    description='Subdomain wordlist generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shriyanss/subdomain_wordlist_gen',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'subgen = subgen.cli:main',
        ],
    }
)
