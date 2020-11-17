#!/usr/bin/python3

from segments_processor import SegmentsProcessor
from functions_processor import FunctionsProcessor
from segment_function_processor import SegmentFunctionProcessor

import os

def segments_processing(list_seg_a, list_seg_b):
    """The function processes two list of segments to find the overlap."""
    segments = SegmentsProcessor(list_seg_a, list_seg_b)
    # results of overlap
    overlap = segments.find_overlap()
    print("The result of the overlap:", overlap)

def functions_processing(list_func_a, list_func_b):
    """The function processes two list of functions to compute pearson correlation."""
    # process two functions
    functions= FunctionsProcessor(list_func_a, list_func_b)
    # result of pearson correlation
    r = functions.compute_pearson_correlation()
    print("Pearson correlation:", r)

def segment_function_processing(list_seg, list_func):
    """The function compute the mean of covered positions."""
    # process one segment and one function
    segment_function = SegmentFunctionProcessor(list_seg, list_func)
    # result of mean
    mean_covered_positions = segment_function.compute_mean_covered_positions()
    print("mean of covered positions:", mean_covered_positions)

def create_data_list(file_directory_name, file_names, f):
    """The function creates data list from input files."""
    list_data = []
    for file_name in file_names:
        file_to_open = file_directory_name+'/'+file_name
        try:
            with open(file_to_open, 'r') as input_file:
                input_file_data = [f(each_line) for each_line in input_file]
                list_data.append(input_file_data)
        except IOError as err:
            print("input file err:", str(err))
    return list_data

def get_file_names(file_dir):
    """The function gets segment and function file names in a directory."""
    segment_file_names = []
    function_file_names = []
    try:
        for f_name in os.listdir(file_dir):
            if f_name.endswith('.s'):
                segment_file_names.append(f_name)
            if f_name.endswith('.f'):
                function_file_names.append(f_name)
    except FileNotFoundError as err:
        print("input file directory err:", str(err))
    return segment_file_names, function_file_names

if __name__ == '__main__':
    # tasks start
    # get files from the directory
    file_dir = 'testfiles'
    segment_file_names, function_file_names = get_file_names(file_dir)

    # task 1
    # function to cover data type
    string_to_int_list = lambda each_line: list(map(lambda x: int(x), each_line.strip().split('\t'))) # '1  2' -> [1, 2]
    # create lists of segments
    list_segments = create_data_list(file_dir, segment_file_names, string_to_int_list)
    # process two segment data
    """TODO: Currently for each type (s or f file), there are only two files in the
    directory, so here simply directory access them. If there are more files for
    each type, then need to loop through them to process and analyze."""
    print("--- Processing segment files %s and %s:" % (segment_file_names[0], segment_file_names[1]))

    segments_processing(list_segments[0], list_segments[1])

    # task 2
    # function to cover data type
    string_to_float = lambda each_line: float(each_line.strip()) # '1' -> 1
    # create lists of functions
    list_functions = create_data_list(file_dir, function_file_names, string_to_float)
    # process two function data
    """TODO: Currently for each type (s or f file), there are only two files in the
    directory, so here simply directory access them. If there are more files for
    each type, then need to loop through them to process and analyze."""
    print("--- Processing function files %s and %s:" % (function_file_names[0], function_file_names[1]))

    functions_processing(list_functions[0], list_functions[1])

    # task 3
    # combinations store all possible combinations of s and f files' name and
    # data recorded in dictionary.
    combinations = []
    length = len(list_segments) * len(list_functions)
    for i in range(length):
        idx_segment = int((i + 2) / 2) - 1  # 0, 0, 1, 1
        idx_function = (i + 2) % 2          # 0, 1, 0, 1
        # combine file name and file data into a dictionary
        combination = {segment_file_names[idx_segment]: list_segments[idx_segment],
                function_file_names[idx_function]: list_functions[idx_function]}
        combinations.append(combination)

    for combination in combinations:
        segment_file_name, function_file_name = tuple(combination.keys())
        print("--- Processing a segment file %s and a function file %s:" %
                (segment_file_name, function_file_name))
        list_segment = combination[segment_file_name]
        list_function = combination[function_file_name]
        # process a segment file and a function data
        segment_function_processing(list_segment, list_function)

