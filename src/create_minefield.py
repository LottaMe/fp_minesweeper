from .create_grid import create_grid

def create_minefield(rows:int, cols:int, mines: list[int]) -> list[list]:
    return _place_mines(
        grid=create_grid(rows=rows, cols=cols), 
        mines=mines, 
        cols=cols
    )

def _place_mines(grid: list[list[None]], mines: list[int], cols: int)->list:
    mines_indexes = [_generate_mine_index(cols=cols, mine=mine) for mine in mines]
    return [
        [
            'm' if (i, j) in mines_indexes else cell for j, cell in enumerate(row)
        ] 
        for i, row in enumerate(grid)
    ]

def _generate_mine_index(cols: int, mine: int):
    return (mine//cols, mine%cols)
