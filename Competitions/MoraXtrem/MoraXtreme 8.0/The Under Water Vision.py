def find_perpendicular_bisector_equation(point1, point2):
    # Calculate the midpoint of the line segment.
    midpoint = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

    # Calculate the slope of the original line.
    if point1[0] != point2[0]:
        original_slope = -(point2[1] - point1[1]) / (point2[0] - point1[0])
    else:
        original_slope = float('inf')  # Vertical line

    # Calculate the negative reciprocal of the original slope to find the perpendicular bisector slope.
    if original_slope == 0:
        perpendicular_slope = float('inf')  # Vertical line
    elif original_slope == float('inf'):
        perpendicular_slope = 0  # Horizontal line
    else:
        perpendicular_slope = -1 / original_slope

    # Calculate the y-intercept "c" using the midpoint and perpendicular slope.
    c = midpoint[1] - perpendicular_slope * midpoint[0]

    return perpendicular_slope, c

def find_tectonic_margin_parameters(image_frame):
    # Create lists to store coordinates of black pixels.
    black_pixels_x = []
    black_pixels_y = []
    white_pixel_x = []
    white_pixel_y = []
    
    # Convert the binary image frame into a list of coordinates of black pixels.
    for y in range(len(image_frame)):
        for x in range(len(image_frame[y])):
            if image_frame[y][x] == "1":
                black_pixels_x.append(x)  # Flip the y-coordinate
                black_pixels_y.append(len(image_frame) - y - 1)  # Flip the y-coordinate
            else:
                white_pixel_x.append(x)  # Flip the y-coordinate
                white_pixel_y.append(len(image_frame) - y - 1)  # Flip the y-coordinate
    
    black_point = []
    black_point.append(sum(black_pixels_x)/len(black_pixels_x))
    black_point.append(sum(black_pixels_y)/len(black_pixels_y))

    white_point = []
    white_point.append(sum(white_pixel_x)/len(white_pixel_x))
    white_point.append(sum(white_pixel_y)/len(white_pixel_y))

    return find_perpendicular_bisector_equation(black_point, white_point)


t = int(input())

for _ in range(t):
    space = input()
    
    img = []
    for i in range(50):
        img.append(input())
        
    tectonic_margin_parameters = find_tectonic_margin_parameters(img)
    print(tectonic_margin_parameters[0], tectonic_margin_parameters[1])
    