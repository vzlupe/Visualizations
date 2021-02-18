import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1, 5=Big5): "))
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1","Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats","Big5Stats"]
	slash = "\\"

	stats = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Stats.csv")
	stats2 = stats.loc[(stats.xa>1.99)]
	stats3 = stats2.loc[(stats.minutes>699)]

	coef = np.polyfit(stats3["minutes"],stats3["xa"],1)
	poly1d_fn = np.poly1d(coef)

	fig, ax = plt.subplots()
	fig.set_size_inches(7,5)
	plt.plot(stats3["minutes"],stats3["xa"],"o")
	ax.set_title("xA/Min")
	ax.set_ylabel("xA")
	ax.set_xlabel("Minutes")
	for x,y,p in zip(stats3["minutes"],stats3["xa"],stats3["player"]):
		label = p
		if (y>2.5):
			ax.annotate(label,
						(x,y),
						textcoords="offset points",
						xytext=(0,4),
						ha='center',
						size=6)
	plt.plot(stats3["minutes"], poly1d_fn(stats3["minutes"]), 'k-', linestyle = (0, (1, 10)), lw=1)
	plt.show()

if __name__ == '__main__':
	main()