import os
import zipfile
import cv2
import numpy as np
from tqdm import tqdm

def extract_and_preprocess(zip_path, output_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    image_files = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
    processed_images = []

    for image_file in tqdm(image_files):
        image = cv2.imread(os.path.join(output_dir, image_file))
        image = cv2.resize(image, (128, 128))
        processed_images.append(image)

    np.save(os.path.join(output_dir, "processed_images.npy"), processed_images)
    print(f"Preprocessing complete. Processed images saved to {output_dir}")

if __name__ == "__main__":
    zip_path = "data_pipeline/raw_data/eurosat.zip"
    output_dir = "data_pipeline/processed_data"
    extract_and_preprocess(zip_path, output_dir)
