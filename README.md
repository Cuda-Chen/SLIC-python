# SLIC-python
A naive SLIC superpixel implementation in Python.

## Install dependencies
```
$ pip install -r requirements.txt
```

## Run
```
usage: main.py [-h] [-o OUTPUTIMAGE] [-iter ITERATIONS]
               inputimage num_pixel compactness

Demo of SLIC superpixel.

positional arguments:
  inputimage            path of input image
  num_pixel             number of initial superpixles
  compactness           compactness factor

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUTIMAGE, --outputimage OUTPUTIMAGE
                        path of output image
  -iter ITERATIONS, --iterations ITERATIONS
                        number of SLIC iterations
```
