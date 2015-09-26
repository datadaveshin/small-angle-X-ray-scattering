#!/usr/bin/env python
"""
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
or
./image_subract.py  <--- provided path is set correctly on line 1
"""

#import modules
import sys
import itertools
sys.path.insert(0,"/usr/local/dectris/albula/3.1/python")
import dectris.albula
import math
import matplotlib.pyplot as plt
import numpy as np

# User variables to define image paths and number of exposures
PATH_FILE_PREFIX = "/data/kburnett/090415Water/Water_"
LIST_OF_WELL_NUMBERS = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
PATH_FILE_SUFFIX = "_1.tif"
NUMBER_OF_EXPOSURES = 5

# User output choices
PRINT_TABLE =  True    # True or False
PLOT_HEATMAP = True    # True or False

def make_series_list(prefix, image_list, suffix):
    """Function takes in the well/image list, and information about the files path and 
    makes a list of Series objects, where each well or image set is contained in one 
    series object. Each object with the list then contains individual images that 
    corresponds to each exposure time. A list of lists with the image set name and the
    series objects is then returned. 
    """  
    
    series_list = []
    for image in image_list:
        path = prefix + image + suffix         # assemble the path for image series 
        #print "path: ", path
        series = dectris.albula.DImageSeries() # get the series object
        series.open(path)
        series_obj = series
        list_pair = [image, series]            # make a two-element list with image set name, series obj 
        series_list.append(list_pair)          # build a list of lists upon each iteration
    #print series_list
    return series_list                         # return the list of lists


def compare_as_table(lst):
    """Function takes in a list of lists that consists of image set names and series objects and
    returns the mean of the difference of image pairs 
    """

    for idx in range(NUMBER_OF_EXPOSURES):
        exposure = idx + 1
        print 26 * "#"
        print "exposure", exposure 
        for x, y in itertools.combinations(lst, 2):
            img1 = x[1][exposure]
            img2 = y[1][exposure]
            diff = img1 - img2
            fmt = 'img {0:>3} - img {1:>3} = {2:>6.3f}'
            print fmt.format(x[0], y[0], diff.mean())
        print "\n"


def plot_it(titl, data_arr):
     """Function takes in an array consisting of a list of lists and 
     plots the data in the form of a heatmap. A title is also required.
     Axis labels are read in from the user defined LIST_OF_WELL_NUMBERS
     Parts of this function were derived from an answer here:
     http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor
     """
    
     # convert to numpy array and set up plot 
     data = np.array(data_arr)
     fig, ax = plt.subplots()
     heatmap = ax.pcolor(data, cmap=plt.cm.Reds)

     # read in axis labels
     row_labels = LIST_OF_WELL_NUMBERS
     column_labels = LIST_OF_WELL_NUMBERS

     # put the major ticks at the middle of each cell
     ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
     ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

     # create table-like display
     ax.set_title(titl, y = 1.08)
     ax.invert_yaxis()
     ax.xaxis.tick_top()
     ax.set_xticklabels(row_labels, minor=False)
     ax.set_yticklabels(column_labels, minor=False)

     # plot
     plt.show()


def compare_as_grid(lst):
    """Function takes in a list of lists that consists of image set names and series objects and
    returns the mean of the difference of image pairs in the form of a grid that can be used for
    a heatmap.
    """

    for idx1 in range(NUMBER_OF_EXPOSURES):
        exposure = idx1 + 1
        title =  "Exposure " + str(exposure)
        data_array = []
        for idx2 in range(len(lst)):
            img1 = lst[idx2][1][exposure]
            row = []
            for idx3 in range(len(lst)):
                img2 = lst[idx3][1][exposure]
                diff = img1 - img2
                mean_abs_val = math.fabs(diff.mean())
                row.append(mean_abs_val)
            data_array.append(row)
        print title, "\n", data_array, "\n"   # Comment out if you don't want to print the grids
        plot_it(title, data_array)


def run():
     """ Runs the program. First it defines the path and file names of images, then either 
     makes a table or heatmap plot, depending on what the user wants.
     """

     series_lst = make_series_list(PATH_FILE_PREFIX, LIST_OF_WELL_NUMBERS, PATH_FILE_SUFFIX)
     #print series_lst
     if PRINT_TABLE:
         compare_as_table(series_lst)
     if PLOT_HEATMAP:
         compare_as_grid(series_lst)


run()
