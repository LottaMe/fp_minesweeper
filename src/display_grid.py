class IOMonad:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def __str__(self):
        return str(self.value)
    
def display_grid(grid: list[list]) -> IOMonad:
    return IOMonad('\n'.join(map(str, grid)))

