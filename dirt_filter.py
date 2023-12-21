from PIL import Image, ImageDraw, ImageEnhance
import random
import os

def add_noise(image, width, height, color_range):
    draw = ImageDraw.Draw(image)
    for _ in range(int(width * height * 0.1)):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        random_color = (random.randint(0, color_range), random.randint(0, color_range), random.randint(0, color_range))
        draw.point((x, y), fill=random_color)

def add_custom_dirt(image, width, height):
    draw = ImageDraw.Draw(image, 'RGBA')
    num_dirt_spots = 100

    for _ in range(num_dirt_spots):
        x = random.randint(0, width)
        y = random.randint(0, height)
        dirt_size = random.randint(5, 20)
        dirt_color = (39, 23, 22, random.randint(100, 200))
        draw.ellipse((x, y, x + dirt_size, y + dirt_size), fill=dirt_color)

def add_dirt_to_image(image_path, output_path):
    base_image = Image.open(image_path)
    width, height = base_image.size

    add_noise(base_image, width, height, 255)
    add_custom_dirt(base_image, width, height)

    enhancer = ImageEnhance.Brightness(base_image)
    dirty_image = enhancer.enhance(0.8)

    dirty_image.save(output_path)

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_dirty.jpg")
            add_dirt_to_image(image_path, output_path)
            print(f"Processed {filename}")

process_directory('PATH')
