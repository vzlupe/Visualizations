import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
	league = int(input("Choose league (0=Prem, 1=Bundes, 2=LaLiga, 3=SerieA, 4=Ligue1): "))
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1"]#,"Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats"]#,"Big5Stats"]
	slash = "\\"

	stats = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Stats.csv")
	defense = pd.read_csv(leagues1[league] + slash + leagues2[league] + "Defense.csv")
	defense["minutes"] = stats["minutes"]
	defense2 = defense.loc[(defense.minutes>699)]
	defense3 = defense2.loc[(defense2.tackles_interceptions>15)]

	fig, ax = plt.subplots()
	fig.set_size_inches(7,5)

	coef = np.polyfit(defense3["tackles_interceptions"],defense3["minutes"],1)
	poly1d_fn = np.poly1d(coef)

	plt.plot(defense3["tackles_interceptions"],defense3["minutes"],"o")
	ax.set_title("Tackles & Interceptions/Min")
	ax.set_xlabel("Tackles & Interceptions")
	ax.set_ylabel("Minutes")



	for x,y,p in zip(defense3["tackles_interceptions"],defense3["minutes"],defense3["player"]):
		label = p
		if (x>45):
			ax.annotate(label,
						(x,y),
						textcoords="offset points",
						xytext=(0,4),
						ha='center',
						size=6)
	plt.plot(defense3["tackles_interceptions"], poly1d_fn(defense3["tackles_interceptions"]), 'k-', linestyle = (0, (1, 10)), lw=1)
	plt.show()

if __name__ == '__main__':
	main()