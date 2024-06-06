import requests
import zipfile
import os

# URL of the ZIP file
url = "https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip"

# Destination directory to extract the files
destination_dir = "files"

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Send a GET request with headers to download the ZIP file
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"  # Replace with your actual User-Agent string
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the ZIP file
    zip_path = os.path.join(destination_dir, "submissions.zip")
    with open(zip_path, "wb") as zip_file:
        zip_file.write(response.content)

    # Extract the contents of the ZIP file
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(destination_dir)

    # Remove the ZIP file
    os.remove(zip_path)

    print("Extraction completed.")
else:
    print("Failed to download the ZIP file.")
