"""
 Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
   
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

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        
        self._height = grid_height
        self._width = grid_width
        self.reset()
        self._init_tile = {UP: [(0,col) for col in range(self._width)],
                          DOWN:[(self._height - 1,col) for col in range(self._width)],
                          LEFT:[(row, 0) for row in range(self._height)],
                          RIGHT:[(row, self._width - 1) for row in range(self._height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cell = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._width)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == LEFT or direction == RIGHT :
            length = self._width 
        if direction == UP or direction == DOWN:
            length = self._height 
        update_flag = False
        
        for tile in self._init_tile[direction]:
            temp_list = []
            for dummy_i in range(length):
                temp_list.append(self._cell[tile[0] + dummy_i * OFFSETS[direction][0]][tile[1] + dummy_i * OFFSETS[direction][1]])
            temp_list_merge = merge(temp_list)
            if temp_list_merge != temp_list:
                update_flag = True
            for dummy_i in range(length):
                self._cell[tile[0] + dummy_i * OFFSETS[direction][0]][tile[1] + dummy_i * OFFSETS[direction][1]] = temp_list_merge[dummy_i]
        if update_flag:
            self.new_tile() 

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        values = [2 for dummy_element in range(9)] + [4]
        non_zero = False
        while (not non_zero):
            p_x = random.choice(range(self._width))
            p_y = random.choice(range(self._height))
            if not self._cell[p_y][p_x]:
                self._cell[p_y][p_x] = random.choice(values) 
                break
               

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cell[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cell[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 6))
print(str(TwentyFortyEight(5, 6)))