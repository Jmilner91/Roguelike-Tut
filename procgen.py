import random
from typing import Iterator, Tuple

import tcod

from game_map import GameMap
import tile_types

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

def tunnel_between( #Function takes 2 arguments & returns an Iterator of a Tuple of 2 ints - Tuples will be x and y coordinates on the map.
        start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these 2 points"""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5: # 50% chance. Picks between 2 options, moving horiz then vert, or opposite. Based on the choice, corner_x and corner_y are set to different points.
        # Move horizontally, then vertically
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally
        corner_x, corner_y = x1, y2

    # Generate the coordinates for the tunnel
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y



def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    for x, y in tunnel_between(room_2.center, room_1.center):
        dungeon.tiles[x, y] = tile_types.floor
        
    return dungeon