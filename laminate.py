from model.tile import Tile
from model.room import Room
from model.installation import Installation
from ui.printer import Printer


def main():
    room = Room(8420, 3795)
    tile = Tile(1380, 244)
    border = 8
    init_tiles = dict()
    n_start_tiles = 3
    for i in range(n_start_tiles):
        init_tiles[i] = (i+1) * tile.length/n_start_tiles

    installation = Installation(room, tile, border, init_tiles, reuse_tiles=True)
    plan = installation.process()
    installation.print()
    Printer.print(plan)


if __name__ == '__main__':
    main()
