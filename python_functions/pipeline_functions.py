import os
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import pickle

def read_eeg_file(filepath):
    eeg_data = {}
    
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            channel = parts[0]
            values = [float(value) for value in parts[1:] if value]
            eeg_data[channel] = values
        
    return eeg_data

def parse_filename(filename):
    base_name = os.path.splitext(filename)[0]
    parts = base_name.split('_')
    synset_id = parts[3]
    image_number = parts[4]
    session_number = parts[5]
    global_session_number = parts[6]
    
    return {
        'synset_id': synset_id,
        'image_number': image_number,
        'session_number': session_number,
        'global_session_number': global_session_number
    }
    
def get_image_path(info, image_root_dir):
    synset_id = info['synset_id']
    image_number = info['image_number']
    image_filename = f"{synset_id}_{image_number}.JPEG"
    image_path = os.path.join(image_root_dir, synset_id, image_filename)
    return image_path

def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(f"Image not found: {image_path}")
        return None
    

        