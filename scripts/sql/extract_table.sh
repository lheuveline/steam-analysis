#!/bin/bash

TABLE_NAME=$1
OUTPUT_FILE=$2


mysql -h steam-analysis.cvkio2p2ho8s.eu-west-3.rds.amazonaws.com \
	-u admin -p steam_analysis \
	-e "SELECT * FROM $TABLE_NAME;" | sql2csv > $OUTPUT_FILE
