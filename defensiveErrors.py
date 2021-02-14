import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1): "))
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"]#,"Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats"]#,"Big5Stats"]
	slash = "\\"

	stats = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Defense.csv")
	stats2 = stats.loc[(stats.errors>1)]

	fig, ax = plt.subplots()
	fig.set_size_inches(7,5)
	plt.bar(x=np.arange(0,len(stats2.index)),height=stats2["errors"])
	ax.set_title("Defensive Errors")
	ax.set_ylabel("Errors")
	plt.xticks(np.arange(0,len(stats2.index)), stats2["player"], rotation=90)
	plt.xlabel("Player")
	plt.show()

if __name__ == '__main__':
	main()