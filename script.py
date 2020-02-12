#!/usr/bin/env python3
"""Automated Installation Script
"""

import datetime, os, sys
we_are_in_heroku = os.environ.get('CLEARDB_DATABASE_URL', None) is not None

import bootstrap_helpers as bh

def main(argv = []):
    if we_are_in_heroku:
        name = 'run_' + str(datetime.datetime.now()).replace(' ', '_') + '.log'
        print('Environment is Heroku with CLEARDB, stdout to %s' % (name))
        sys.stdout = file(name, 'w')

    bh.remove_env()
    print('Removed env')

    bh.create_env()
    print('Created env')

    bh.use_env()
    print('Used env')
    
    packages = []
    packages.append(['bs4', 'bs4'])
    packages.append(['inquirer', 'inquirer'])
    packages.append(['sqlalchemy', 'SQLAlchemy'])
    packages.append(['pymysql', 'pymysql'])
    packages.append(['psycopg2', 'psycopg2'])
    packages.append(['requests', 'requests'])
    bh.install_missing(packages)
    print('Installed missing packages')

    import helpers as h
    print('Imported helpers')

    result = h.drop_and_create()
    print('Imported helpers: ' + str(result))
    h.install()


if __name__ == '__main__':
    main(sys.argv)
