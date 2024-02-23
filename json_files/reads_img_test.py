# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:05:24 2023

@author: USER
"""
from flask import Flask, request, render_template ,json, jsonify
import os
import struct
import numpy as np
from PIL import Image

from io import BytesIO,StringIO

file_name = 'C:/Users/USER/Downloads/test1/json_files/test_img1.png'

with open(file_name,'rb') as f:
    
    pixel = f.read()

with open("./saveTest_save1.json") as f:
        imgbuffer = json.load(f)
        
# img = Image.open(BytesIO(imgbuffer['data']))