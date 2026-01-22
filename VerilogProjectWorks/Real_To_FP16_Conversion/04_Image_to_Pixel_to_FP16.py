from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\Owner\Desktop\smile1.jpeg").convert("L")
img = img.resize((100, 100))

pixels = np.array(img)

with open("image_fp16.mem", "w") as f:
    for y in range(100):
        for x in range(100):
            val = float(pixels[y, x])
            fp16 = np.float16(val)
            hex_val = fp16.view(np.uint16)
            f.write(f"{hex_val:04X}\n")

print("image_fp16.mem generated")
