with open("Day 02/input.txt", "r") as fp:
    data = fp.readlines()

total = 0
for row in data:
    l, w, h = [int(dimension) for dimension in row.strip().split("x")]

    surface_areas = [2*l*w, 2*w*h, 2*h*l]
    smallest_surface_area = min(surface_areas) / 2

    required_paper = sum(surface_areas) + smallest_surface_area
    total += required_paper

print(int(total))
