"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    result_list = [0] * len(line)
    find_merge = False
    flag_index = []
    
    # merge same element (from left to right)
    for dummy_i in range(len(line)):
        if line[dummy_i] != 0 and dummy_i not in flag_index:
            for dummy_j in range(dummy_i + 1, len(line)):
                if line[dummy_i] == line[dummy_j]:
                    result_list[dummy_i] = line[dummy_i] * 2
                    find_merge = True
                    flag_index.append(dummy_j)
                    break
                elif line[dummy_j] != 0:
                    break
                dummy_j += 1
                
            if not find_merge:
                result_list[dummy_i] = line[dummy_i]
            find_merge = False
            
        dummy_i += 1
    
    # move to the left
    for dummy_i in range(len(result_list)):
        if result_list[dummy_i] != 0:
            dummy_i += 1
        else:
            for dummy_j in range(dummy_i + 1, len(line)):
                if result_list[dummy_j] != 0:
                    result_list[dummy_i] = result_list[dummy_j]
                    result_list[dummy_j] = 0
                    break
                dummy_j += 1
            dummy_i += 1
    
                         
    
    return result_list