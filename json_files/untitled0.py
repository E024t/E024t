# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:53:23 2023

@author: USER

python -c "import sys; print(sys.executable)"
"""
from flask import Flask, request, render_template ,json, jsonify
import os



with open("./account.json") as f:
        SignUPdata = json.load(f)

a = [{"account":"jaw123","code":"123"}]
