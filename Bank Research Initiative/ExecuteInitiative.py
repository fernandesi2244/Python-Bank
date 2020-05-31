from DownloadDataset import DownloadDataset as Downloader

dataset = 'barelydedicated/bank-customer-churn-modeling'
csvName = 'Churn_Modelling.csv'
fileDir = 'Bank Research Initiative'

downloader = Downloader(dataset, csvName, fileDir)
fileName = downloader.downloadFile()

downloadedFile = downloader.getDownloadedFile()
if(downloadedFile is None):
    print("Couldn't locate downloaded csv file... Please try again!")
    exit()