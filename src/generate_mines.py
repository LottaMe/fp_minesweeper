import random

def generate_mines(rows: int, cols: int, mine_count: int) -> list[int]:
    return random.sample(range(0, rows*cols), mine_count)