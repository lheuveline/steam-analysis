# Export table as csv file

SELECT * FROM Achievement_Percentages
INTO OUTFILE './achievement_percentages.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ';'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n'

