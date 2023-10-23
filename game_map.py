import numpy as np #type: ignore
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F") #Creates a 2D array filled with values from tile_types.floor that filles self.tiles with floor tiles.

        self.tiles[30:33, 22] = tile_types.wall #creates small, 3 tile wide wall at specified location. Demonstrative.

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside the bounds of this map"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
