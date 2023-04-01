import colorgram

colors = colorgram.extract('image.jpg', 10)
color_palette = []

c1 = colors[0]
print(c1.rgb)

c2 = colors[1]
print(c2.rgb)

c3 = colors[2]
print(c3.rgb)

c4 = colors[3]
print(c4.rgb)
