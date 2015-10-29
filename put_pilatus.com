#!/bin/csh
# David Shin ©10-29-2015
#
# Script controls the buffer subtraction  perl script
#
# Use sed to change rows:
# :1,$s/A/B/g
# to change from A to B.
#
# Set exposure numbers in the foreach argument list.
# For four exposures, this should look like this:
# foreach i (1 2 3 4)
#
# Check and modify to make sure you are subtracting correct buffers
# from samples.
#
# Comment out wells if not being used:
# #PutPilatus *_A12_{$i}.tif buff_*_A11_{$i}.tif
#
# Redirect to produce an output file:
# ./put_pilatus.com > results.out
#####################################

cat put_pilatus.com

foreach i ( 1 2 3 4 5)  #<-- change for exposure numbers, ex. 3 exp is (1 2 3 4)
    PutPilatus *_A2_{$i}.tif buff_*_A1_{$i}.tif
    PutPilatus *_A4_{$i}.tif buff_*_A3_{$i}.tif
    PutPilatus *_A6_{$i}.tif buff_*_A5_{$i}.tif
    PutPilatus *_A8_{$i}.tif buff_*_A7_{$i}.tif
#    PutPilatus *_A10_{$i}.tif buff_*_A9_{$i}.tif
#    PutPilatus *_A12_{$i}.tif buff_*_A11_{$i}.tif
