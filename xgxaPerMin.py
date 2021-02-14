import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1): "))
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"]#,"Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats"]#,"Big5Stats"]
	slash = "\\"

	stats = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Stats.csv")
	stats["xgxa"] = stats.xg+stats.xa
	stats2 = stats.loc[(stats.xgxa>1.99)]
	stats3 = stats2.loc[(stats.minutes>699)]

	fig, ax = plt.subplots()
	fig.set_size_inches(7,5)
	plt.plot(stats3["xgxa"],stats3["minutes"],"o")
	ax.set_title("xG+xA/Min")
	ax.set_xlabel("xG+xA")
	ax.set_ylabel("Minutes")
	for x,y,p in zip(stats3["xgxa"],stats3["minutes"],stats3["player"]):
		label = p
		if (x>4.99):
			ax.annotate(label,
						(x,y),
						textcoords="offset points",
						xytext=(0,4),
						ha='center',
						size=6)
	plt.plot([2,20],[699,2000],'k-', linestyle = ":", lw=1)
	plt.show()

if __name__ == '__main__':
	main()