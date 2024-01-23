square_area = lambda s: s ** 2
rectangle_area = lambda l, w: l * w
triangle_area = lambda b, h: 0.5 * b * h
par = lambda s: 4*s
print("Area of square:", square_area(5))
print("Area of rectangle:", rectangle_area(4, 7))
print("Area of triangle:", triangle_area(6, 8))
print("par is", par(3))
print("Area of square:", square_area(10))