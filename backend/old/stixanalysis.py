import os
import json
import stix2viz
from tkinter import filedialog
from tkinter import *

def parse_json():
    
    root = Tk()
    root.filename = filedialog.askopenfilename(
        initialdir="/Desktop", title="Select file", filetypes=(("json files", "*.json"), ("all files", "*.*")))
    print(root.filename)
    #file_extension = os.path.splittext(root.filename) # fetch the file extension
    #if file_extension != '.json': # check if file extension is json format
    #    print('INVALID FILE SELECTED.')
    #else:
    with open(root.filename, 'r') as f:
        json_data = json.load(f) # parsing the json file to a python object
    #print(json_data)    
    stix2viz.display(json_data)
        

output = parse_json()
print(output)