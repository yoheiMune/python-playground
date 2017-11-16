# Sample Usage for python virtual enviroment.
Using `venv` which is enabled at Python 3.3+.

## How to use it.
### Create.
Create a new virtual env.
```
# python3 -m venv /path/to/new/virtual/environment
$ python3 -m venv env1
```
```
# For Windows.
# c:\>c:\Python35\python -m venv c:\path\to\myenv
```
Check the items created.
```
$ ls -la env1
total 8
drwxr-xr-x   6 munesadayohei  staff  192 11 16 09:23 .
drwxr-xr-x   4 munesadayohei  staff  128 11 16 09:23 ..
drwxr-xr-x  12 munesadayohei  staff  384 11 16 09:23 bin
drwxr-xr-x   2 munesadayohei  staff   64 11 16 09:23 include
drwxr-xr-x   3 munesadayohei  staff   96 11 16 09:23 lib
-rw-r--r--   1 munesadayohei  staff  114 11 16 09:23 pyvenv.cfg
```
### Activate.
Step in the directory.
```
$ cd env1
```
Activate the enviroment.
```
# for bash (like MacOSX).
$ source bin/activate

# for Windows.
C:\> <venv>\Scripts\activate.bat
```
See the detail in [venv document](https://docs.python.jp/3/library/venv.html).
### Check the activated result.
`python` and `pip` commands in this enviroment are used.
```
$ which python
/tmp/env1/bin/python
$ which pip
/tmp/env1/bin/pip
```
Check the pathes.
```
$ python
>>> import sys, pprint; pprint.pprint(sys.path)
[
 '',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',
 '/tmp/env1/lib/python3.6/site-packages'
]
```
You can find `env1/lib/python3.6/site-packages` directory. This is the private site-package for the enviroment you created.

Also,
```
$ pip freeze
# Nothing...
```
No packages are installed in your enviroment.

### Deactivate
```
$ deactivate
```

## Helps.
```
$ python3 -m venv -h
```

## References.
* [https://docs.python.jp/3/library/venv.html](https://docs.python.jp/3/library/venv.html)