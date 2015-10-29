# saxs
This repository contains scripts for small-angle X-ray scattering
The scripts are for aiding processing SAXS data or to deal with the hardware at SIBYLS beamline 12.3.1.

put_pilatus.com - A simple shell script to control the buffer subtraction software to process your images.

image_subtract.py - This takes a series of Dectris Pilatus 2M SAXS .tif images, where each series has multiple
exposures, calculates the differences between each pixel for pairs of images that
have the same exposure time. Then outputs the mean or a heat map. 
Basically, this is used to compare what should be series of images (with different exposures) that 
correspond to the same type of sample for trouble shooting purposes. Say shooting 12 water samples at 
4 different exposure settings. 
