#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script outputs content of database tables in the file

post_query = ['psql', '-U', 'postgres', 'test_bd', '-c',
                        'SELECT * FROM test_table;']


class Extractor(object):
    def __init__(self, query):
        self.query = query

    def extinfile(self):
        import subprocess
        from datetime import date

        outquery = subprocess.Popen(self.query, stdout=subprocess.PIPE).communicate()[0]

        dt = date.today()
        with open('/ARCHIVE/list_unis_%s.%s.%s.txt' % (dt.year, dt.month, dt.day), 'wt') as fout:
            fout.write(outquery)


if __name__ == "__main__":
    Extractor(post_query).extinfile()
