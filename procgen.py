from typing import Tuple

class RectangularRoom: #class used to create rooms
    def __init__(self, x: int, y: int, width: int, height: int): #takes x&y coordinates of the top left corner & computes the bottom right corner based on width & height parameters
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

        @property
        def center(self) -> Tuple[int, int]: #center is a property which is a read-only variable for the RectangularRoom class. It describes x & y coords of center of the room
            center_x = int((self.x1 + self.x2) / 2)
            center_y = int((self.y1 + self.y2) / 2)

            return center_x, center_y
        
        @property
        def inner(self) -> Tuple[slice, slice]: #inner is a property that returns 2 slices that are the inner portion of our room that's 'dug out' via the dungeon generator and provides the area to carve out.
            '''Return the inner area of this room as a 2D array index'''
            return slice(self.x1 + 1, self.x2), slice(self.y1 +1, self.y2) #ensures that if 2 rooms are next to one another, a wall will be accounted for
        