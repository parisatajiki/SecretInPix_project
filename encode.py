from PIL import Image

image_url = "img/01.png"
text = " Hello World "
img = Image.open(image_url).convert("RGB")

text_idx = 0
text_len = len(text)
done = False
step = 10

for y in range(0, img.size[1], step):
    for x in range(0, img.size[0], step):
        if text_idx < text_len:
            chr = text[text_idx]
            rgb = (ord(chr), 0, 0)
            img.putpixel((x, y), rgb)
            text_idx += 1
        else:
            img.putpixel((x, y), (0, 0, 255))
            done = True
            break
    if done:
        break

img.save("img/02.png")