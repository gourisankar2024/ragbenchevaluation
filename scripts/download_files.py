import os
import requests
from tqdm import tqdm

GITHUB_API_URL = "https://api.github.com/repos/chen700564/RGB/contents/data"
RAW_BASE_URL = "https://raw.githubusercontent.com/chen700564/RGB/master/data/"
LOCAL_SAVE_PATH = "data"

os.makedirs(LOCAL_SAVE_PATH, exist_ok=True)

def get_file_list():
    """Fetch the list of files from the GitHub repository."""
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        return [file["name"] for file in response.json() if file["name"].startswith("en")]
    else:
        print("Failed to fetch file list:", response.text)
        return []

def download_file(file_name):
    """Download a single file and save it locally."""
    file_url = RAW_BASE_URL + file_name
    local_file_path = os.path.join(LOCAL_SAVE_PATH, file_name)

    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        with open(local_file_path, "wb") as file, tqdm(
            total=total_size, unit="B", unit_scale=True, desc=file_name
        ) as progress:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progress.update(len(chunk))
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download {file_name}: {response.status_code}")
