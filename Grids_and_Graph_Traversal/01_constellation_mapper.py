

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:

    grid = []
    for _ in range(dim):
        nested = []
        for _ in range(dim):
            nested.append(".")
        grid.append(nested)

    for row, col in stars:
        if col < 0 or col >= dim or row < 0 or row >= dim:
            continue
        grid[row][col] = "*"

    res = []
    for cell in grid:
        s = ""
        for c in cell:
            s += c
        res.append(s)
        
    return res
    

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
print(constellation_mapper([], 2))
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
print(constellation_mapper([(0, 0), (5, 5)], 3))
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))

ss = "this is test"
sss = ss.replace("t", "b")
print(sss)