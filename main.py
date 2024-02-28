from src.create_minefield import create_minefield
from src.generate_mines import generate_mines
from src.create_grid import create_grid
from src.display_grid import display_grid
from src.make_move import make_move
### TRY OUT ###
### Play Game with this minefield:
# minefield = [
#     [None, 'm', None, None, None, None, None, None],
#     [None, None, None, None, None, 'm', 'm', None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, 'm', None, None],
#     [None, None, None, None, None, None, None, None],
#     ['m', None, None, None, None, None, 'm', None],
#     [None, None, None, None, None, 'm', 'm', None],
#     [None, None, None, 'm', 'm', None, None, None]
# ]
# play(minefield=minefield)

### Play Game with generated minefield
## 4x4 grid with 4 randomly placed mines
if (__name__ == "__main__"):
    ROWS = 4
    COLS = 4
    MINE_COUNT = 4

    generated_mines = generate_mines(rows=ROWS, cols=COLS, mine_count=MINE_COUNT)
    generated_minefield = create_minefield(rows=ROWS, cols=COLS, mines=generated_mines)
    grid = create_grid(rows=ROWS, cols=COLS)

    display_grid(grid).bind(print)

    result = make_move(rows=ROWS, cols=COLS, mine_count=MINE_COUNT, grid=grid, minefield=generated_minefield)
    print(result)