import os
import requests

def download_dataset(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Dataset downloaded and saved at {save_path}")
    else:
        print("Failed to download the dataset.")

if __name__ == "__main__":
    url = "https://your-open-source-dataset-url"
    save_path = "data_pipeline/raw_data/eurosat.zip"
    download_dataset(url, save_path)
