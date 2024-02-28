def create_grid(rows: int, cols: int)-> list[list[None]]:
    return [['?' for _ in range(cols)] for _ in range(rows)]
