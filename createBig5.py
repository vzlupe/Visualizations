from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import Comment
import pandas as pd
from pathlib import Path

def main():
	leagues1 = ["Premier League","Bundesliga","La Liga","Serie A","Ligue 1","Big 5"]
	leagues2 = ["PremierLeagueStats","BundesligaStats","LaLigaStats","SerieAStats","Ligue1Stats","Big5Stats"]
	count = [0,1,2,3,4]#,5]
	slash = "\\"


	PStats = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Stats.csv")
	BStats = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Stats.csv")
	LaStats = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Stats.csv")
	LiStats = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Stats.csv")
	SStats = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Stats.csv")
	ComboStats = pd.concat([PStats,BStats,LaStats,LiStats,SStats])
	ComboStats.to_csv(leagues1[5] + slash + leagues2[5] + "Stats.csv")

	PKeepers = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Keepers.csv")
	BKeepers = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Keepers.csv")
	LaKeepers = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Keepers.csv")
	LiKeepers = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Keepers.csv")
	SKeepers = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Keepers.csv")
	ComboKeepers = pd.concat([PKeepers,BKeepers,LaKeepers,LiKeepers,SKeepers])
	ComboKeepers.to_csv(leagues1[5] + slash + leagues2[5] + "Keepers.csv")

	PKeepersadv = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Keepersadv.csv")
	BKeepersadv = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Keepersadv.csv")
	LaKeepersadv = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Keepersadv.csv")
	LiKeepersadv = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Keepersadv.csv")
	SKeepersadv = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Keepersadv.csv")
	ComboKeepersadv = pd.concat([PKeepersadv,BKeepersadv,LaKeepersadv,LiKeepersadv,SKeepersadv])
	ComboKeepersadv.to_csv(leagues1[5] + slash + leagues2[5] + "Keepersadv.csv")

	PMisc = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Misc.csv")
	BMisc = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Misc.csv")
	LaMisc = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Misc.csv")
	LiMisc = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Misc.csv")
	SMisc = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Misc.csv")
	ComboMisc = pd.concat([PMisc,BMisc,LaMisc,LiMisc,SMisc])
	ComboMisc.to_csv(leagues1[5] + slash + leagues2[5] + "Misc.csv")

	PPassing = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Passing.csv")
	BPassing = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Passing.csv")
	LaPassing = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Passing.csv")
	LiPassing = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Passing.csv")
	SPassing = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Passing.csv")
	ComboPassing = pd.concat([PPassing,BPassing,LaPassing,LiPassing,SPassing])
	ComboPassing.to_csv(leagues1[5] + slash + leagues2[5] + "Passing.csv")

	PPassing_types = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Passing_types.csv")
	BPassing_types = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Passing_types.csv")
	LaPassing_types = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Passing_types.csv")
	LiPassing_types = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Passing_types.csv")
	SPassing_types = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Passing_types.csv")
	ComboPassing_types = pd.concat([PPassing_types,BPassing_types,LaPassing_types,LiPassing_types,SPassing_types])
	ComboPassing_types.to_csv(leagues1[5] + slash + leagues2[5] + "Passing_types.csv")

	PPlayingtime = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Playingtime.csv")
	BPlayingtime = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Playingtime.csv")
	LaPlayingtime = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Playingtime.csv")
	LiPlayingtime = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Playingtime.csv")
	SPlayingtime = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Playingtime.csv")
	ComboPlayingtime = pd.concat([PPlayingtime,BPlayingtime,LaPlayingtime,LiPlayingtime,SPlayingtime])
	ComboPlayingtime.to_csv(leagues1[5] + slash + leagues2[5] + "Playingtime.csv")

	PPossession = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Possession.csv")
	BPossession = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Possession.csv")
	LaPossession = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Possession.csv")
	LiPossession = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Possession.csv")
	SPossession = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Possession.csv")
	ComboPossession = pd.concat([PPossession,BPossession,LaPossession,LiPossession,SPossession])
	ComboPossession.to_csv(leagues1[5] + slash + leagues2[5] + "Possession.csv")

	PGca = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Gca.csv")
	BGca = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Gca.csv")
	LaGca = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Gca.csv")
	LiGca = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Gca.csv")
	SGca = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Gca.csv")
	ComboGca = pd.concat([PGca,BGca,LaGca,LiGca,SGca])
	ComboGca.to_csv(leagues1[5] + slash + leagues2[5] + "Gca.csv")

	PShooting = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Shooting.csv")
	BShooting = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Shooting.csv")
	LaShooting = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Shooting.csv")
	LiShooting = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Shooting.csv")
	SShooting = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Shooting.csv")
	ComboShooting = pd.concat([PShooting,BShooting,LaShooting,LiShooting,SShooting])
	ComboShooting.to_csv(leagues1[5] + slash + leagues2[5] + "Shooting.csv")

	PDefense = pd.read_csv(leagues1[0] + slash + leagues2[0] + "Defense.csv")
	BDefense = pd.read_csv(leagues1[1] + slash + leagues2[1] + "Defense.csv")
	LaDefense = pd.read_csv(leagues1[2] + slash + leagues2[2] + "Defense.csv")
	LiDefense = pd.read_csv(leagues1[3] + slash + leagues2[3] + "Defense.csv")
	SDefense = pd.read_csv(leagues1[4] + slash + leagues2[4] + "Defense.csv")
	ComboDefense = pd.concat([PDefense,BDefense,LaDefense,LiDefense,SDefense])
	ComboDefense.to_csv(leagues1[5] + slash + leagues2[5] + "Defense.csv")

if __name__ == '__main__':
	main()