import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1): "))
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"]#,"Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats"]#,"Big5Stats"]
	slash = "\\"

	stats = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Stats.csv")
	stats2 = stats.loc[(stats.xg>0)]
	stats3 = stats2.loc[(stats2.minutes>0)]
	stats4 = stats3.loc[stats3["squad"] == "Southampton"]
	stats5 = stats3.loc[stats3["squad"] == "Leeds United"]
	combo = [stats4,stats5]
	result = pd.concat(combo)

	fig, ax = plt.subplots()
	fig.set_size_inches(7,5)

	coef = np.polyfit(result["minutes"],result["xg"],1)
	poly1d_fn = np.poly1d(coef)

	plt.plot(result["minutes"],result["xg"],"o")
	ax.set_title("xG/Min - Southampton & Leeds")
	ax.set_ylabel("xG")
	ax.set_xlabel("Minutes")
	for x,y,p,z in zip(result["minutes"],result["xg"],result["player"],result["squad"]):
		label = p
		if (y>0):
			ax.annotate(label,
						(x,y),
						textcoords="offset points",
						xytext=(0,4),
						ha='center',
						size=6)
	plt.plot(result["minutes"], poly1d_fn(result["minutes"]), 'k-', linestyle = (0, (1, 10)), lw=1)
	plt.show()

if __name__ == '__main__':
	main()