# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, send_file, jsonify
from io import StringIO, BytesIO
import os, glob, sys
import json, random, base64, time as timelib
import datetime, shutil, csv, io
from urllib.request import urlopen
import urllib, requests, re
from bs4 import BeautifulSoup
import urllib.request as urllib2
from flask import Response, make_response, current_app

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/static/index.html")

@app.route('/wdired_listdir', methods=["PUT", "POST"])
def listdir():
    data = request.get_json(force=True)   
    dir_par = data['dir']
    subdirs = [x for x in os.listdir(dir_par) if os.path.isdir(os.path.join(dir_par, x))]
    subfiles = [x for x in os.listdir(dir_par) if os.path.isfile(os.path.join(dir_par, x))]
    res = {"dirs": subdirs, "files": subfiles}
    return jsonify(res)

@app.route('/wdired_copy', methods=["PUT", "POST"])
def wdired_copy():
    data = request.get_json(force=True)   
    fromDir = data['fromDir']
    checkedItems = data['checkedItems']
    toDir = data['toDir']
    print (fromDir, checkedItems, toDir)
    for item in checkedItems:
        fr_curr = fromDir + "/" + item
        if os.path.isdir(fr_curr):
            shutil.copytree(fr_curr, toDir + "/" + item)
        if os.path.isfile(fr_curr):
            shutil.copy(fr_curr, toDir)
            
    return jsonify("ok")

@app.route('/wdired_move', methods=["PUT", "POST"])
def wdired_move():
    data = request.get_json(force=True)   
    fromDir = data['fromDir']
    checkedItems = data['checkedItems']
    toDir = data['toDir']
    print (fromDir, checkedItems, toDir)
    for item in checkedItems:
        fr_curr = fromDir + "/" + item
        shutil.move(fr_curr, toDir)
            
    return jsonify("ok")

@app.route('/wdired_delete', methods=["PUT", "POST"])
def wdired_delete():
    data = request.get_json(force=True)   
    fromDir = data['fromDir']
    checkedItems = data['checkedItems']
    print (fromDir, checkedItems)
    for item in checkedItems:
        fr_curr = fromDir + "/" + item
        if os.path.isdir(fr_curr):
            print ("removing dir", fr_curr)
            shutil.rmtree(fr_curr)
        if os.path.isfile(fr_curr):
            print ("removing file", fr_curr)
            os.remove(fr_curr)
                        
    return jsonify("ok")

@app.route('/get_file/<farg>')
def get_file(farg):
    filename = base64.decodestring(bytes(farg,'utf-8')).decode('utf-8')
    print ('read file',filename)
    if (".txt" in filename or ".md" in filename):
        return Response(open(filename).read(), mimetype='text/plain')
    elif (".jpg" in filename):
        return send_file(filename, mimetype='image/jpg')
    elif (".png" in filename):
        return send_file(filename, mimetype='image/png')
    elif (".pdf" in filename):
        binary_pdf = open(filename,"rb").read()
        response = make_response(binary_pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
        return response
    elif (".mp4" in filename):

        binary_vid = open(filename,"rb").read()
        response = make_response(binary_vid)
        response.headers['Content-Type'] = 'video/mp4'
        response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % 'yourfilename'
        return response
        
        
if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost",port=5000)

