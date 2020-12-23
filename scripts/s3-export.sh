#!/bin/bash

#aws s3 sync s3://ndx-steam-analysis/mysql_export/steam_analysis.Friends/ \
#	./data/s3-export/steam_analysis.Friends --profile steam-export-2 --sse AES256

aws s3 sync s3://ndx-steam-analysis/mysql_export/steam_analysis.Games_1/ \
        ./data/s3-export/steam_analysis.Games_1 --profile steam-export-2 --sse AES256

aws s3 sync s3://ndx-steam-analysis/mysql_export/steam_analysis.Games_2/ \
        ./data/s3-export/steam_analysis.Games_2 --profile steam-export-2 --sse AES256

aws s3 sync s3://ndx-steam-analysis/mysql_export/steam_analysis.Games_Daily/ \
        ./data/s3-export/steam_analysis.Games_Daily --profile steam-export-2 --sse AES256

aws s3 sync s3://ndx-steam-analysis/mysql_export/steam_analysis.Player_Summaries/ \
        ./data/s3-export/steam_analysis.Player_Summaries --profile steam-export-2 --sse AES256
