#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script outputs content of database tables in the file
# Contents:
# - ID session (session_id)
# - Name session (session_name)
# - Unis (uni_name)
# - User (login)
# - Open/Close (state, 2 - close / 1 - open)
# - Rights session (rights_session)

import subprocess
from datetime import date

post_query = ['psql', '-U', 'postgres', 'sorm_psi', '-c',
                        'SELECT * FROM (SELECT unse.session_id, unse.session_name, unse.state, unse.uni_name, us.login FROM\
                                        (SELECT se.session_id, se.name session_name, se.state, se.owner_id, un.name uni_name FROM sessions se\
                                                        INNER JOIN unis un USING (session_id) WHERE se.options = 2 and se.state in (1, 2) ORDER BY se.name) unse\
                                                INNER JOIN users us ON (unse.owner_id = us.user_id)) one\
                                        INNER JOIN (SELECT session_id, array_agg(login) rights_session FROM\
                                                                (SELECT se.session_id, us.login from sessions se INNER JOIN sessions_rights sr USING (session_id)\
                                                                        INNER JOIN users us USING (user_id) WHERE se.options = 2 and se.state in (1, 2)) as sesrus GROUP BY session_id) two\
                                        USING (session_id);']


class Extractor(object):
    def __init__(self, query):
        self.query = query

    def extinfile(self):
        import subprocess
        from datetime import date

        outquery = subprocess.Popen(self.query, stdout=subprocess.PIPE).communicate()[0]
        outquery = outquery.replace('|     1 |', '|  open |')
        outquery = outquery.replace('|     2 |', '| close |')

        dt = date.today()

        with open('/ARCHIVE/list_unis_%s.%s.%s.txt' % (dt.year, dt.month, dt.day), 'wt') as fout:
            fout.write(outquery)


if __name__ == "__main__":
    Extractor(post_query).extinfile()
