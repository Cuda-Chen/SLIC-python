#!/usr/local/bin/python

import argparse as args
from slic_superpixel import slic

parser = args.ArgumentParser(description='Demo of SLIC superpixel.')
parser.add_argument('inputimage', help='path of input image')
parser.add_argument('-o', '--outputimage', required=False, help='path of output image')
parser.add_argument('num_pixel', help='number of initial superpixles')
parser.add_argument('compactness', help='compactness factor')
parser.add_argument('-iter', '--iterations', required=False, default=10, help='number of SLIC iterations')
ap = vars(parser.parse_args())

myslic = slic.Slic(ap['inputimage'], int(ap['num_pixel']), int(ap['compactness']))
myslic.iterate(int(ap['iterations']))
myslic.show_image()
