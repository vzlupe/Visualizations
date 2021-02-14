from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
from pathlib import Path

def main():
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"]#,"Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats"]#,"Big5Stats"]
	count = [0,1,2,3,4]#,5]
	slash = "\\"

	for x in count:
		minutes = pd.read_csv(leagues1[x] + slash + leagues2[x] + "Stats.csv")
		minutes['minutes'] = minutes['minutes'].apply(sanitize_mins)
		minutes.to_csv(leagues1[x] + slash + leagues2[x] + "Stats.csv")

def sanitize_mins(mins):
	mins_as_string = str(mins)
	mins_sanitized = mins_as_string.replace(',','')
	return int(mins_sanitized)

if __name__ == '__main__':
	main()