HOST=$1
USER=$2
DATABASE=$3

pv data/steam.sql.gz | gunzip | mysql \
	-h $HOST \
	-u $USER \
	-p $DATABASE
