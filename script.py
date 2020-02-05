#!/usr/bin/env python3
"""Automated Installation Script
"""

import sys

import bootstrap_helpers as bh

def main(argv = []):
    # bh.remove_env()
    # bh.create_env()
    bh.use_env()

    
    packages = []
    packages.append(['bs4', 'bs4'])
    packages.append(['inquirer', 'inquirer'])
    packages.append(['sqlalchemy', 'SQLAlchemy'])
    packages.append(['pymysql', 'pymysql'])
    packages.append(['psycopg2', 'psycopg2'])
    bh.install_missing(packages)

    import helpers as h

    # result = h.get_sql_flavor()
    # print("got result: " + result)
    # h.drop_and_create()
    print(h.get_database_name())




if __name__ == '__main__':
    main(sys.argv)
