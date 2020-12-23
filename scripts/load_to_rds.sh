pv data/steam.sql.gz | gunzip | mysql \
	-h steam-analysis.cvkio2p2ho8s.eu-west-3.rds.amazonaws.com \
	-u admin \
	-p steam_analysis
