def update_user_grid(user_grid: list[list], minefield: list[list], coord:tuple[int, int]) -> list[list]:
    if _check_for_mine(minefield=minefield, coord=coord):
        return [[]]
    elif user_grid[coord[0]][coord[1]] == '?':
        n = _calculate_field(minefield, coord)
        updated_user_grid = user_grid.copy()
        updated_user_grid[coord[0]][coord[1]] = n
        return updated_user_grid
    else:
        return user_grid
    
def _calculate_field(minefield: list[list], coord: tuple[int, int]) -> str:
    surrounding_fields = _generate_surrounding_fields(minefield, coord)
    count = sum(map(lambda f: _check_for_mine(minefield, f), surrounding_fields))

    return str(count)

def _generate_surrounding_fields(grid: list[list], coord:tuple[int, int]) -> list[tuple]:
    x_length = len(grid)
    y_length = len(grid[0])
    surrounding_fields = [
        (coord[0]-1, coord[1]-1),
        (coord[0]-1, coord[1]),
        (coord[0]-1, coord[1]+1),
        (coord[0], coord[1]-1),
        (coord[0], coord[1]+1),
        (coord[0]+1, coord[1]-1),
        (coord[0]+1, coord[1]),
        (coord[0]+1, coord[1]+1),
    ]
    return filter(lambda f: _check_valid_field(f, x_length, y_length), surrounding_fields)

def _check_for_mine(minefield: list[list], coord: tuple[int, int]) -> bool:
    return minefield[coord[0]][coord[1]] == 'm'

def _check_valid_field(coord: tuple[int, int], x: int, y: int) -> bool:
    if coord[0] >= x or coord[0] < 0:
        return False
    if coord[1] >= y or coord[1] < 0:
        return False
    return True