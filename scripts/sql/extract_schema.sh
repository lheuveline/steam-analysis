#!/bin/bash

mysqldump -h steam-analysis.cvkio2p2ho8s.eu-west-3.rds.amazonaws.com \
	-u admin \
	-p --no-data --databases steam_analysis > schema.sql

