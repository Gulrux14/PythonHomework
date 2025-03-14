import numpy as np
from PIL import Image

# Rasmni yuklash
image_path = "images/birds.jpg"
image = Image.open(image_path)

# Rasmni NumPy arrayga o‘girish
image_array = np.array(image)

# 1. Rasmni gorizontal va vertikal ag‘darish
flipped_image = np.flipud(np.fliplr(image_array))

# 2. Tasodifiy shovqin qo‘shish
noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
noisy_image = np.clip(image_array + noise, 0, 255)

# 3. Yorqinlikni oshirish
brightness_increase = 40
brightened_image = np.clip(image_array + brightness_increase, 0, 255)

# 4. Markaziy 100x100 maydonni qora rang bilan yopish
h, w, _ = image_array.shape
center_x, center_y = w // 2, h // 2
mask_size = 100
masked_image = image_array.copy()
masked_image[
    center_y - mask_size // 2 : center_y + mask_size // 2,
    center_x - mask_size // 2 : center_x + mask_size // 2,
] = 0

# Natijalarni saqlash
Image.fromarray(flipped_image).save("output/flipped_birds.jpg")
Image.fromarray(noisy_image).save("output/noisy_birds.jpg")
Image.fromarray(brightened_image).save("output/brightened_birds.jpg")
Image.fromarray(masked_image).save("output/masked_birds.jpg")

print("Barcha tasvirlar muvaffaqiyatli saqlandi!")