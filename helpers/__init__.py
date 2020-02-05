import os
from six.moves.urllib import parse

local = 'postgres://toor:root@localhost/electoral'
CONNECTION_STRING = os.environ.get('CLEARDB_DATABASE_URL', local)

PREFIX = 'electoral_wiki'

def get_database_name(connection_string=CONNECTION_STRING):
    return parse.urlparse(connection_string).path.replace('/', '')

from .prompts import get_sql_flavor

from .database import drop_and_create

# from .wiki_requests import 
