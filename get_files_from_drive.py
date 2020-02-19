import argparse
import requests
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    save_response_content(response, destination)
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None
def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_id', help='the ID of the file to download')
    parser.add_argument('dest_name', help='the name of the file to download into')
    args = parser.parse_args()
    file_id = args.file_id
    destination = args.dest_name
    print("Downloading ID '%s' to file '%s'" % (file_id, destination))
    download_file_from_google_drive(file_id, destination)