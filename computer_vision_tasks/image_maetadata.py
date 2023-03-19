from PIL import Image
from PIL.ExifTags import TAGS
 
# open the image
imagename = "img.jpg"

# read the image data using PIL
image = Image.open(imagename)

# extract other basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label,value in info_dict.items():
    print(f"{label:20}: {value}")

# extracting the exif metadata
exifimg = image.getexif()
 
# iterating over all EXIF data fields
for tag_id in exifimg:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    img_data = exifimg.get(tag_id)
    # decode bytes 
    if isinstance(img_data, bytes):
        img_data = img_data.decode()
    print(f"{tag:25}: {img_data}")