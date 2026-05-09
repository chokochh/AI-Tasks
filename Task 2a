colors = ["Red", "Green", "Blue"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA"],
}

assigned = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assigned and assigned[neighbor] == color:
            return False
    return True

def solve(regions):
    if len(assigned) == len(regions):
        return True

    unassigned = [r for r in regions if r not in assigned]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color):
            assigned[region] = color

            if solve(regions):
                return True

            del assigned[region]

    return False

regions = list(neighbors.keys())

if solve(regions):
    print("Australia Map Colouring Solution:\n")
    for region in assigned:
        print(region, "->", assigned[region])
else:
    print("No solution found.")
