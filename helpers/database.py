import re
from six.moves.urllib import parse

import sqlalchemy
from sqlalchemy import create_engine

from . import CONNECTION_STRING, PREFIX

def drop_and_create(prefix=PREFIX, connection_string=CONNECTION_STRING):
    while True:
        print('Connecting to DB: ' + connection_string)
        engine = create_engine(connection_string)
        try:
            names = engine.table_names()
            to_drop = []
            for name in names:
                if name.index(prefix) == 0:
                    to_drop.append(name)

            print('Found ' + str(len(to_drop)) + ' tables to drop')
            for name in to_drop:
                engine.execute('drop table ' + name)

            return True

        except (sqlalchemy.exc.InternalError, sqlalchemy.exc.OperationalError) as e:
            message = getattr(e, 'message', repr(e))

            regex = r"database ['\"]([^'\"']*)['\"]"
            matches = re.search(regex, message, re.MULTILINE)

            # our database is not created
            if matches is not None:
                missing_database = matches.group(1)
                print('Database ' + missing_database + ' was not found, creating...')

                parsed = parse.urlparse(connection_string)._asdict()
                applied = dict(parsed, path='/')
                temp_connection_string = parse.ParseResult(**applied).geturl()

                temp_engine = create_engine(temp_connection_string)
                conn = temp_engine.connect()

                if temp_connection_string.startswith('postgres'):
                    conn.execute("commit")

                conn.execute("create database " + missing_database)
                continue

            else:
                print('InternalError or OperationalError which is not a missing database')
                return False

        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            return False
