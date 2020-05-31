from kaggle.api.kaggle_api_extended import KaggleApi
from os import listdir

class DownloadDataset(object):
    def __init__(self, dataset, csvName, fileDir):
        self.dataset = dataset
        self.csvName = csvName
        self.fileDir = fileDir
        self.api = KaggleApi()
        self.api.authenticate()

    def downloadFile(self):
        if(self.getDownloadedFile() is None):
            self.api.dataset_download_file(self.dataset, self.csvName, self.fileDir)
            print('File successfully downloaded! Proceeding...')
        else:
            print('The csv file has already been downloaded! Proceeding...')

    def getDownloadedFile(self):
        for entry in listdir('Bank Research Initiative'):
            if '.csv' in entry:
                return entry