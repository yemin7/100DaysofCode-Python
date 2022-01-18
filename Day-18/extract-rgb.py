import colorgram as cg

colors = cg.extract('spot-painting.jpg', 10)
rgb_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    rgb_color.append(rgb)

print(rgb_color)


#[(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50)]