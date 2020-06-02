from kaggle.api.kaggle_api_extended import KaggleApi
from os import listdir

class DownloadDataset(object):
    def __init__(self, dataset, csv_name, file_dir):
        self.dataset = dataset
        self.csv_name = csv_name
        self.file_dir = file_dir
        self.api = KaggleApi()
        self.api.authenticate()

    def download_file(self):
        if(self.get_downloaded_file() is None):
            self.api.dataset_download_file(self.dataset, self.csv_name, self.file_dir)
            print('File successfully downloaded! Proceeding...\n')
        else:
            print('The csv file has already been downloaded! Proceeding...\n')

    def get_downloaded_file(self):
        for entry in listdir('Bank Research Initiative'):
            if '.csv' in entry:
                return entry
