from PIL import Image

image_url = "img/02.png"
img = Image.open(image_url)

text = ""
done = False
for y in range(0, img.size[1], 10):
    for x in range(0, img.size[0], 10):
        r, g, b = img.getpixel((x, y))
        if r == 0 and b == 255:
            done = True
            break
        text += chr(r)
    if done:
        break

print("Decoded text: ", text)