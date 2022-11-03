import requests
from zipfile import ZipFile

def download_data(URL,fileName,path):
    # download the data
    response = requests.get(URL)
    # Open the response into a new file called "OtwartyWroclaw_rozklad_jazdy_GTFS.zip"
    open(fileName, "wb").write(response.content)
    # Extracting all the members of the zip into a specific location.
    with ZipFile(fileName, "r") as zip_ref:
        zip_ref.extractall(path)
    return(URL)

# List of all files in folder
# list_of_files = os.listdir(path)
# print(list_of_files)
