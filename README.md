# testdataengine
Tool for generating input data for testing


## Usage
```
$ ./main.py -h
usage: main.py [-h] [-p] [-n] [-e]

A tool for generating input data. Use stand-alone or in an existing workflow
to supply data.

optional arguments:
  -h, --help   show this help message and exit
  -p, --pnr    Generate Personal Number
  -n, --name   Generate Personal Name
  -e, --email  Generate Personal Email
```

## Installation
To install the package with distutils use 
```
$ python ./setup.py install --user
```

## Burp
To use testdataengine as a burp plugin you need to manully move the file `burptestdatagenerator.py` and the folder `testdatagenerator` to the folder burp uses to load modules. When they are moved there, they can be loaded as any other python extension.