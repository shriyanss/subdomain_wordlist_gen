# subdomain_wordlist_gen (aka subgen)
Subdomain wordlist generator

## Table of contents
- [Installation](#installation)
    - [Install using `pip` (recommended)](#install-using-pip-recommended)
    - [Install using `setup.py` file](#install-using-setuppy-file)
- [Usage](#usage)
    - [Generate a simple wordlist using the given subdomains file](#generate-a-simple-wordlist-using-the-given-subdomains-file)

## Installation
### Install using `pip` (recommended)
```
pip install subgen
```
OR
```
pip3 install subgen
```

**NOTE: When tested on mac OS, installing without sudo didn't worked as expected, so consider running above commands as root instead**

### Install using `setup.py` file
```
sudo python setup.py install
```
OR
```
sudo python3 setup.py install
```

## Usage
```
usage: subgen-runner.py [-h] -i INPUT [-s] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file to generate wordlist with
  -s, --silent          Don't print the banner
  -o OUTPUT, --output OUTPUT
                        Output file to write the wordlist
```

### Generate a simple wordlist using the given subdomains file
This will split and then print the results.

Example:-
```
$ cat subdomains.txt
www.example.com
blog.example.com
store.example.com
forum.example.com
support.example.com
news.example.com
app.example.com
mail.example.com
forum.example.com
events.example.com
partners.example.com
```
```
$ subgen -i subdomains.txt
               __                   
   _______  __/ /_  ____ ____  ____ 
  / ___/ / / / __ \/ __ `/ _ \/ __ \
 (__  ) /_/ / /_/ / /_/ /  __/ / / /
/____/\__,_/_.___/\__, /\___/_/ /_/ 
                 /____/             

www
blog
store
forum
support
news
app
mail
events
partners
```