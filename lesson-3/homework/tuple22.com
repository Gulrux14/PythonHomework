def create_range_tuple(start, end): 
 return tuple(range(start, end + 1))