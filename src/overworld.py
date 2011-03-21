"""Functions and classes related to the overworld.
"""
class Tile:
    isWalkable = False
    contains = []

    def remove(self, thing):
        if thing in contains:
            try:
                contains.remove(thing)
            except ValueError:
                pass


class Overworld:
    _tiles = {}

    def __repr__(self):
        S = ""
        # Find maximum i and j
        max_i = 0
        max_j = 0
        for (i,j) in self._tiles.keys():
            if i > max_i: max_i = i
            if j > max_j: max_j = j

        for i in range(max_i+1):
            for j in range(max_j+1):
                if self.tileExists(i,j):
                    S += "X"
                else:
                    S += " "
            S += "\n"

        return S

    def addTile(self, tile, x, y):
        self._tiles[(x,y)] = tile

    def tileExists(self, x, y):
        try:
            if self._tiles[(x,y)] is not None:
                return True
        except KeyError:
            return False



if __name__ == "__main__":
    world = Overworld()
    world.addTile(Tile(), 0, 0)
    world.addTile(Tile(), 7, 0)
    world.addTile(Tile(), 0, 7)
    world.addTile(Tile(), 3, 4)
    world.addTile(Tile(), 4, 4)
    print world
