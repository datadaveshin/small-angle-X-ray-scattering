DATE:
Fri Sep 11 15:26:56 PDT 2015

AUTHORS:
David Shin, Scott Classen

DESCRIPTION:
Script takes a series of dectris SAXS .tif images, where each series has multiple
exposures, calculates the differences between each pixel for pairs of images that
have the same exposure time. Then outputs the mean.

User must supply the path and file name in the following manner as shown for the
example below:

for image file series:
/data/kburnett/090415Water/Water_A1_1.tif
/data/kburnett/090415Water/Water_A1_2.tif
/data/kburnett/090415Water/Water_A1_3.tif
/data/kburnett/090415Water/Water_A2_1.tif
/data/kburnett/090415Water/Water_A2_2.tif
/data/kburnett/090415Water/Water_A2_3.tif

the user would input:
PATH_FILE_PREFIX = "/data/kburnett/090415Water/Water_"
LIST_OF_WELL_NUMBERS = ['A1', 'A2'] <--- note you can expand this list to multiple images
PATH_FILE_SUFFIX = "_1.tif"
NUMBER_OF_EXPOSURES = 5

USAGE:
python image_subtract.py

