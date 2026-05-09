colors = ["Red", "Green", "Blue", "Yellow"]

neighbors = {
    "Westlands": ["Dagoretti North", "Starehe", "Ruaraka"],
    "Dagoretti North": ["Westlands", "Dagoretti South"],
    "Dagoretti South": ["Dagoretti North", "Langata"],
    "Langata": ["Dagoretti South", "Kibra"],
    "Kibra": ["Langata", "Starehe"],
    "Starehe": ["Westlands", "Kibra", "Kamukunji"],
    "Kamukunji": ["Starehe", "Makadara"],
    "Makadara": ["Kamukunji", "Embakasi West"],
    "Embakasi West": ["Makadara", "Embakasi Central"],
    "Embakasi Central": ["Embakasi West", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi South"],
    "Embakasi South": ["Embakasi East", "Embakasi North"],
    "Embakasi North": ["Embakasi South", "Ruaraka"],
    "Ruaraka": ["Westlands", "Embakasi North", "Mathare"],
    "Mathare": ["Ruaraka", "Kasarani"],
    "Kasarani": ["Mathare", "Roysambu"],
    "Roysambu": ["Kasarani"]
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
    print("Nairobi Sub-County Colouring Solution:\n")

    for region in assigned:
        print(region, "->", assigned[region])
else:
    print("No solution found.")

