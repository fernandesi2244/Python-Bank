from DownloadDataset import DownloadDataset as Downloader
from StatsAnalysis import StatsAnalysis

dataset = 'barelydedicated/bank-customer-churn-modeling'
csv_name = 'Churn_Modelling.csv'
file_dir = 'Bank Research Initiative'

downloader = Downloader(dataset, csv_name, file_dir)
downloader.download_file()

downloaded_file = downloader.get_downloaded_file()
if(downloaded_file is None):
    print("Couldn't locate downloaded csv file... Please fix the problem and try again!")
    exit()

stats_analyzer = StatsAnalysis(downloaded_file)
stats_analyzer.display(columns=['Age', 'EstimatedSalary'], indexing_value='Surname', num_rows = 20)
stats_analyzer.regression('Age', 'EstimatedSalary', num_points=500)
stats_analyzer.five_num_summary('Balance')
