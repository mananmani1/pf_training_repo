import io
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


def postgre_task():
    images = []
    dataset = "test.zip"

    with ZipFile(dataset,'r') as zip:
        zip.extractall()
    file_name = [os.path.splitext(filename)[0] for filename in os.listdir('test')][4]
    print('Name of files:',file_name)
    for dirpath, dirnames, files in os.walk('test'):
        print(f'Found directory: {dirpath}')
        file_path=os.path.abspath(os.path.join(files[4]))
        print(file_path)
    # for f_path in files:
    #     file_path=os.path.abspath(os.path.join(f_path))
    #     print(file_path)
    # for root, dirs, files in os.walk('test'):
    #     if len(files) > 0:
    #         first_file_path = os.path.join(root, files[0])
    #         print(first_file_path)

    # print(first_file_in_folder)
  
    for img in glob.glob("test/*.jpg"):
        embeded_img = get_embeddings(img)
        print(embeded_img)
    cursor.execute("INSERT INTO File_Detail(File_Name, File_Path,Img_embedding) VALUES (%s, %s, %s)", (str(file_name), str(file_path),str(embeded_img)))
    
    
    conn.commit()
# #Closing the connection
    conn.close()
postgre_task()

