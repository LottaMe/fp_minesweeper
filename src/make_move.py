from functools import reduce
from .display_grid import display_grid
from .update_user_grid import update_user_grid

def make_move(rows: int, cols: int, mine_count: int, grid: list[list], minefield: list[list]) -> str:
    user_row = _get_valid_input(rows, input("Enter a number between 0 and " + str(rows) + ":    "))
    user_col = _get_valid_input(cols, input("Enter a number between 0 and " + str(cols) + ":    "))

    updated_grid = update_user_grid(user_grid=grid, minefield=minefield, coord=(user_row, user_col))
    
    
    if updated_grid == [[]]:
        return "You Lost!"
    elif _check_win(grid=updated_grid, mine_count=mine_count):
        return "You Won!"
    else:
        display_grid(updated_grid).bind(print)
        return make_move(rows=rows, cols=rows, mine_count=mine_count, grid=updated_grid, minefield=minefield)
    
def _check_win(grid: list[list], mine_count:int) -> bool:
    count_row = lambda row: row.count('?')
    hidden_cells = reduce(lambda acc, row: acc + count_row(row), grid, 0)
    return hidden_cells == mine_count

def _get_valid_input(max:int, user_input:str) -> int:
    if(_is_valid_input(
        user_input=user_input, 
        max=max
    )):
        return int(user_input)
    else:
        print("Please enter a number between 0 and " + str(max))
        return _get_valid_input(max=max, user_input=input("Enter a number between 0 and " + str(max) + ":    "))

def _is_valid_input(user_input: str, max: int) -> bool:
    if not user_input.isdigit():
        return False
    if int(user_input) >= max:
        return False
    return True