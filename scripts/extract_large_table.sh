#!/bin/bash

MYSQL=$(mysql -h steam-analysis.cvkio2p2ho8s.eu-west-3.rds.amazonaws.com \
        -u admin -p steam_analysis)

$MYSQL -e "select * from Games_1" | while IFS= read -r ROW
do
    echo "$ROW"
done
