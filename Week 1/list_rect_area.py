lengths = [1, 2, 3, 4]
widths = [2, 3, 4, 5,6]

if len(lengths) == len(widths):
    area = []
    for i in range (0, len(widths)):
        area.append(lengths[i]*widths[i])
    print(area)
else:
    print("god u little shit enter the right numbers")