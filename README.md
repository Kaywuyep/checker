# INTRODUCTION

Hello, this is a mini-project still in it's development phase,
it is a simple python script that automatically formats a code,
run a code-style check then add, commit and push to your Github,
amazing right?!!

## FEATURES
#### Guess what?!!
- this program checks python files with pycodestyle
- checks C/C++ files with betty
- others[.js, .java, .cc files] with black code formatter
- This is tested on Ubuntu 20.04

lets get into it!!!

#### To use this simple program:
1. install YAPF and black code formatters, [fun idea: read about them]
`pip install yapf black`
2. install pycodestyle, betty, and flake8 to check coding style
`pip install flake8  pycodestyle`
> To install betty for C/C++ programs:

`git clone https://github.com/holbertonschool/Betty.git`
`cd Betty`
`sudo ./install.sh`

*NOTE: If you encounter any issues during the installation, be sure to check the Betty repository for any updated instructions or troubleshooting tips.

3. now let the fun begin: clone this repo in the same directory as the files you want to check
`git clone https://github.com/Kaywuyep/checker.git`
`cd checker`
`chmod u+x runchecks`

4. almost done
`mkdir FORMATTER`
`mv *.py __pycache__ README.md FORMATTER/`

5. now we are completly set up:
simply use `./runchecks` filename.py[or any extension available on this program] 'your commit message'

6. kindly `git push` when you are done. And your files are now in you git repository

> I would appreciate any corrections and a fork on this repo.


## THANK YOU!!!!!!!
