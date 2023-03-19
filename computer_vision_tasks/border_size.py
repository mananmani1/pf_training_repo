from PIL import Image, ImageOps

def add_border(image, percentage, color):
    width, height = image.size
    border_size = int(min(width, height) * percentage / 100)
    bordered_image = ImageOps.expand(image, border=(border_size, border_size, border_size, border_size), fill=color)
    return bordered_image

# Get the image path and border percentage from the user
image_path = input("Enter the path to the image file: ")
percentage = float(input("Enter the percentage of the border size: "))
color = input("Enter the border color (white/gray/black): ").lower()

# Map the color input to the RGB values
if color == "white":
    border_color = (255, 255, 255)
elif color == "gray":
    border_color = (128, 128, 128)
elif color == "black":
    border_color = (0, 0, 0)
else:
    print("Invalid color input. Defaulting to white.")
    border_color = (255, 255, 255)

image = Image.open(image_path)

bordered_image = add_border(image, percentage, border_color)

bordered_image.show()
