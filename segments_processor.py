class SegmentsProcessor: 
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def find_overlap(self):
        """This method finds the overlap of the regions from 
        two lists of segments"""

        positions = [] # list stores overlapped positions
        overlap = 0    # the overlap (in number of positions)
        overlap_regions = [] # list stores overlapped regions 

        idx_a = idx_b = 0 # index for list a and b, respectively
        while idx_a < len(self.list_a) and idx_b < len(self.list_b):
            # example: list_a = [[1, 2], [3, 6]] and list_b = [[0, 1], [1, 5]]
            # loop round 1: [1,2] [0,1]
            # loop round 2: [1,2] [1,5]
            # loop round 3: [3,6] [1,5]
            
            start_a, end_a = self.list_a[idx_a]
            start_b, end_b = self.list_b[idx_b]
            # TODO: debug:
            # print("coordinates to compare:", start_a, end_a, " compare to ", start_b, end_b)

            # for current round:
            # check the current two segments from a and b lists to find the overlap
            if end_a > start_b and end_b > start_a:
                ordered_coordinates = sorted([start_a, end_a, start_b, end_b])
                # overlap region is [ordered_coordinates[1], ordered_coordinates[2]]
                # example: region [1,2) in round 2; region [3, 5) in round 3
                overlap_region = [ordered_coordinates[1], ordered_coordinates[2]]
                overlap_regions.append(overlap_region) 
                positions.extend([val for val in
                        range(ordered_coordinates[1], ordered_coordinates[2])])
                # accumulate overlap value
                overlap += ordered_coordinates[2] - ordered_coordinates[1]

            # for next round:
            # the region with lower end coordinate is replaced by next region
            # the region with higher end coordinate stays 
            if end_a < end_b:
                idx_a += 1
            else:
                idx_b += 1
        return overlap

