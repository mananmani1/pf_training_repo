# import pymongo
# from bson.json_util import loads
# from PIL import Image
# import base64
# import os

# # create a connection to your MongoDB server
# client = pymongo.MongoClient("mongodb://localhost:27017/")

# # select a database and collection
# db = client["mydatabase"]
# collection = db["mycollection"]

# # create a JSON object with the image data
# # Set the path to the folder containing the images
# dataset = "test.zip"
#     with ZipFile(dataset,'r') as zip:
#         zip.extractall()

# image_folder = "test"
# with open("image_folder/*.jpg", "rb") as image_file:
#     # Read the image data
#     image_data = image_file.read()
#     # Encode the image data in base64 format
#     encoded_image_data = base64.b64encode(image_data).decode("utf-8")

# # Create the JSON object with the base64-encoded image data
# json_obj = {
#     "imageData": encoded_image_data
# }





# # Get a list of all the image filenames in the folder
# # image_filenames = os.listdir(image_folder_path)

# # Set the index of the image you want to retrieve
# index = 0

# # Get the filename of the image at the specified index
# image_filename = image_filenames[index]

# # Open the image file
# with open(os.path.join(image_folder_path, image_filename), "rb") as image_file:
#     # Read the image data
#     image_data = image_file.read()
#     # Encode the image data in base64 format
#     encoded_image_data = base64.b64encode(image_data).decode("utf-8")

# # Create the JSON object with the base64-encoded image data
# json_obj = {
#     "imageData": encoded_image_data
# }






# # insert the JSON object into the collection
# collection.insert_one(loads(json.dumps(image_data)))
