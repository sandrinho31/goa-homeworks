def calculate_square_properties(side_length=10):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter

square_area1, square_perimeter1 = calculate_square_properties(5)

square_area2, square_perimeter2 = calculate_square_properties()

print("First square - Area:", square_area1, "Perimeter:", square_perimeter1)
print("Second square - Area:", square_area2, "Perimeter:", square_perimeter2)