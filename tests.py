import unittest
from segments_processor import SegmentsProcessor
from functions_processor import FunctionsProcessor
from segment_function_processor import SegmentFunctionProcessor

class Test(unittest.TestCase):

    def test_task_one(self):
        # test data
        list_seg_a = [[1,2],[3,6]]
        list_seg_b = [[0,1],[1,5]]
        # expected result
        expected_overlap = 3

        segments = SegmentsProcessor(list_seg_a, list_seg_b)
        overlap = segments.find_overlap()

        err_info = "Overlap should be " + str(expected_overlap)
        self.assertEqual(overlap, expected_overlap, err_info)

    def test_task_two(self):
        # test data 
        list_func_a = [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
        list_func_b = [10.5, 11.5, 12.0, 13.0, 13.5, 15.0, 14.0]
        expected_pearson_correlation = 0.9452853306994897

        functions = FunctionsProcessor(list_func_a, list_func_b) 
        r = functions.compute_pearson_correlation()
        err_info = "Pearson correlation should be " + str(expected_pearson_correlation)
        self.assertEqual(r, expected_pearson_correlation, err_info)
    
    def test_task_three(self):
        # test data 
        list_seg = [[1,2],[3,6]]
        list_func = [10.5, 11.5, 12.0, 13.0, 13.5, 15.0, 14.0]
        # expected result
        expected_mean = 13.25

        segment_function = SegmentFunctionProcessor(list_seg, list_func)
        mean = segment_function.compute_mean_covered_positions()
        err_info = "mean should be " + str(expected_mean)
        self.assertEqual(mean, expected_mean, err_info)
        

if __name__ == '__main__':
    unittest.main()

