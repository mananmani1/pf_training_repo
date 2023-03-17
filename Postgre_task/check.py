from flask import Flask, render_template, request
import psycopg2
import os
import tqdm
import glob
import traceback
import psycopg2
import pymongo
import gridfs
import bson
from bson.objectid import ObjectId
from flask import Flask
from flask import request
from zipfile import ZipFile
from multiprocessing.pool import ThreadPool
from embeddings import get_embeddings
import pathlib
# from pathlib import pa
import cv2
from postgres_task import  cursor, conn

app = Flask(__name__)

@app.route('/store_data', methods=['POST'])
def store_data():
    dataset = "test.zip"

    with ZipFile(dataset,'r') as zip:
        zip.extractall()
    file_name = [os.path.splitext(filename)[0] for filename in os.listdir('test')][2]
    print('Name of files:',file_name)
    for dirpath, dirnames, files in os.walk('test'):
        print(f'Found directory: {dirpath}')
        file_path=os.path.abspath(os.path.join(files[2]))
        print(file_path)

    image_files = glob.glob("test/*.jpg")
    if len(image_files) < 1:
        print("There are not enough images in the folder")
    else:
        given_image = image_files[2]
        embeded_img = get_embeddings(given_image)
        
        print(embeded_img)
            # embeded_img = get_embeddings(img)
            # print(embeded_img)
   
    # conn = psycopg2.connect(
    #     host='127.0.0.1',
    #     database='postgres',
    #     user='postgres',
    #     password='*postgre0011#'
    # )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO File_Detail(File_Name, File_Path,Img_embedding) VALUES (%s, %s, %s)", (str(file_name), str(file_path),str(embeded_img)))
    
    
    conn.commit()
# #Closing the connection
    conn.close()

    return 'Data stored successfully!'

@app.route('/')
def index():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)




