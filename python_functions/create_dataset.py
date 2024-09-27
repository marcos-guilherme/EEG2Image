#Create Dataset

from python_functions.pipeline_functions import read_eeg_file, parse_filename, get_image_path, load_image
import os
import pickle

eeg_directory = 'data/MindBigData-Imagenet'
eeg_files = [f for f in os.listdir(eeg_directory) if f.endswith('.csv')]


image_root_dir = 'imgs'

dataset = []

for filename in eeg_files:
    file_path = os.path.join(eeg_directory, filename)
    eeg_data =  read_eeg_file(file_path)
    info = parse_filename(filename)
    image_path = get_image_path(info, image_root_dir)
    image = load_image(image_path)
    
    if image:
        sample = {
            'eeg_data':eeg_data,
            'image': image,
            'info': info
        }
        
        dataset.append(sample)
        
with open('eeg_img_dataset.pkl', 'wb') as f:
    pickle.dump(dataset, f)