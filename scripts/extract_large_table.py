from sqlalchemy import create_engine
import os
import csv

import logging
logging.basicConfig(level=logging.INFO, filename = 'logs/export_logs.logs')

from tqdm import tqdm

class TableExporter:

    def __init__(self, **kwargs):

        self.user = kwargs.get('user', 'admin')
        self.password = kwargs.get('password', "Respond01")
        self.host = kwargs.get('host', "steam-analysis.cvkio2p2ho8s.eu-west-3.rds.amazonaws.com")
        self.port = kwargs.get('port', 3306)
        self.dbname = kwargs.get('dbname', "steam_analysis")

        self.conn_str = "mysql+pymysql://{}:{}@{}:{}/{}".format(
            self.user, self.password, self.host, self.port, self.dbname
        )

        self.engine = create_engine(self.conn_str)

        self.logger = logging.getLogger(__class__.__name__)

    def get_table_size(self, table_name):
        r = list(self.engine.execute("SELECT count(*) FROM {}".format(table_name)))[0][0]
        return r

    def get_chunk(self, table_name, start, end):
        q = "SELECT * FROM {} LIMIT {},{}"
        r = list(self.engine.execute(q.format(table_name, start, end)))
        return r

    def export_table(self, table_name, chunk_size = 1e5):
        """ Bulk export table from MySQL and pass to writer function """
        
        table_size = self.get_table_size(table_name)
        step = int(chunk_size)

        self.logger.info('Chunk size = {}'.format(step))

        for i in tqdm(range(0, table_size, step)):
            if i + 1000 < table_size:
                # Get data
                data = self.get_chunk(table_name, i, i + step)
            else:
                data = self.get_chunk(table_name, i, table_size)

            # Write data
            self.write_results("{}.csv".format(table_name), data)

            if i + step < table_size:
                end = i + step
            else:
                end = table_size

            self.logger.info('Exported data from table "{}", from row {} to row {}'.format(
                table_name, i, end
            ))

    def write_results(self, filename, data, data_dir = 'data/rds/'):
        """ Write MySQL query results to specific location """
        
        filepath = os.path.join(data_dir, filename)

        with open(filepath, 'a+') as f:
            writer = csv.writer(f)
            writer.writerows(data)


if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--table', help = 'Table name')
    args = parser.parse_args()

    exporter = TableExporter()
    exporter.export_table(args.table)
