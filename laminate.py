from model.tile import Tile
from model.room import Room
from model.installation import Installation
from ui.printer import Printer


def main():
    room = Room(8420, 3795)
    tile = Tile(1380, 244)
    border = 8
    init = {
        0: 1*1380/3,
        1: 2*1380/3,
        2: 1380
    }

    installation = Installation(room, tile, border, init, True)
    plan = installation.process()
    installation.print()
    Printer.print(plan)


if __name__ == '__main__':
    main()
