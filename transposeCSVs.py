from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
from pathlib import Path

def main():
	leagues = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1","Big 5"]
	for league in leagues:
		csv_folder = Path('D:\\Libraries\\Documents\\GitHub\\FBrefScraper\\' + league + '\\').rglob('*.csv')
		files = [x for x in csv_folder]

		for file in files:
			df = pd.read_csv(file).transpose()
			sp = str(file).split('\\')
			sp[4] = "Visualizations"
			newfile = '\\'.join(sp)
			df.to_csv(newfile,index=False, header=False)

if __name__ == '__main__':
	main()