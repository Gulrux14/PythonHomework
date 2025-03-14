import numpy as np
from PIL import Image

def flip_image(image_array):
    """Rasmni gorizontal va vertikal ag‘darish"""
    return np.flipud(np.fliplr(image_array))

def add_noise(image_array, noise_level=50):
    """Tasodifiy shovqin qo‘shish"""
    noise = np.random.randint(0, noise_level, image_array.shape, dtype=np.uint8)
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, brightness_increase=40):
    """Har bir rang kanalining yorqinligini oshirish"""
    return np.clip(image_array + brightness_increase, 0, 255)

def apply_mask(image_array, mask_size=100):
    """Rasm markazidagi maskani qora rangga o‘zgartirish"""
    masked_image = image_array.copy()
    h, w, _ = image_array.shape
    center_x, center_y = w // 2, h // 2
    masked_image[
        center_y - mask_size // 2 : center_y + mask_size // 2,
        center_x - mask_size // 2 : center_x + mask_size // 2,
    ] = 0
    return masked_image

# Rasmni yuklash va NumPy arrayga o‘girish
image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

# Funksiyalarni chaqirish
flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)

# Natijalarni saqlash
Image.fromarray(flipped_image).save("output/flipped_birds.jpg")
Image.fromarray(noisy_image).save("output/noisy_birds.jpg")
Image.fromarray(brightened_image).save("output/brightened_birds.jpg")
Image.fromarray(masked_image).save("output/masked_birds.jpg")

print("Barcha tasvirlar muvaffaqiyatli saqlandi!")