from six.moves.urllib import parse

# CONNECTION_STRING = 'mysql://root:toor@localhost/electora'
CONNECTION_STRING = 'postgres://toor:root@localhost/electorall'
PREFIX = 'electoral_wiki'

def get_database_name(connection_string=CONNECTION_STRING):
    return parse.urlparse(connection_string).path.replace('/', '')

from .prompts import get_sql_flavor

from .database import drop_and_create

# from .wiki_requests import 
