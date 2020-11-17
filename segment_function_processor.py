class SegmentFunctionProcessor:
    def __init__(self, list_a, list_b):
        """Initialize a list of segment data and a list of function data."""

        self.list_seg = list_a
        self.list_func = list_b

    def compute_mean_covered_positions(self):
        """The method computes mean of covered position numbers."""

        index = [] # list stores index covered by the segment regions
        covered_position_numbers = []
        for region_start, region_end in self.list_seg:
            index.extend(list(range(region_start, region_end)))
        for i in index:
            covered_position_numbers.append(self.list_func[i])
        # TODO: debug:
        #print("index:",index)
        #print("covered positions:", covered_position_numbers)
        return sum(covered_position_numbers)/len(covered_position_numbers)
