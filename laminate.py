from model.tile import Tile
from model.room import Room
from model.installation import Installation
from ui.printer import Printer


def main():
    room = Room(8420, 3795)
    tile = Tile(1380, 244)
    border = 10  # space between tiles and wall
    init_tiles = dict()
    n_start_tiles = 3
    # most used begining sequences, see what fits your room
    # # sequence -> whole tile, tile/3
    # init_tiles[0] = tile.length
    # init_tiles[1] = tile.length/3
    # init_tiles[2] = 2*tile.length/3
    # # sequence -> whole tile, tile/2
    # init_tiles[0] = tile.length
    # init_tiles[1] = tile.length/2
    # # sequence -> 1/n_start_tiles, 2/n_start_tiles, .., whole tile
    # for i in range(n_start_tiles):
    #     init_tiles[i] = (i+1) * tile.length/n_start_tiles
    # # sequence -> whole tile, (n_start_tiles-1)/n_start_tiles, ..., 1/n_start_tiles
    for i, j in enumerate(reversed(range(n_start_tiles))):
        init_tiles[i] = (j+1) * tile.length/n_start_tiles

    installation = Installation(room, tile, border, init_tiles, reuse_tiles=True)
    plan = installation.process()
    installation.print()
    Printer.print(plan)


if __name__ == '__main__':
    main()
