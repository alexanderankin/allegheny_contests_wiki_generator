import os, random, string
from six.moves.urllib import parse

import bs4, requests

from . import CONNECTION_STRING, PREFIX

def format_conn_string(connection_string=CONNECTION_STRING):
    parsed = parse.urlparse(connection_string)
    settings = {}
    settings['host'] = parsed.hostname
    settings['port'] = parsed.port
    settings['user'] = parsed.username
    settings['password'] = parsed.password
    settings['database'] = parsed.path.replace('/', '')
    return settings

def install(base='http://localhostwiki'):
    base_url = base + '/mw-config/index.php'
    def b(part=''):
        return base_url + part

    settings = format_conn_string()
    sess = requests.Session()
    res = language_page(sess, b(), b('?page=Language'))
    res = sess.post(b('?page=Welcome'), data={'submit-continue':'Continue →'})
    res = db_page(sess, settings, res, b('?page=DBConnect'))
    d = {'mysql__SameAccount':'1','submit-continue':'Continue →'}
    res = sess.post(b('?page=DBSettings'), data=d)
    res = name_page(sess, res, b('?page=Name'))
    res = sess.post(b('?page=Install'), data={'submit-continue':'Continue →'})
    res = sess.post(b('?page=Install'), data={'submit-continue':'Continue →'})

    with requests.get(url, stream=True) as r:
        with open('LocalSettings.php', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    print('Saved Settings')

    perms = 'wgGroupPermissions'
    with open('LocalSettings.php', 'a') as f:
        f.write('\n')
        f.write("$" + perms + "['*']['createaccount'] = false;\n")
        f.write("$" + perms + "['user']['createaccount'] = true;\n")
        f.write("$" + perms + "['user']['editinterface'] = true;\n")
        f.write("$" + perms + "['Bureaucrats']['createaccount'] = true;\n")
        f.write("$" + perms + "['sysop']['createaccount'] = true;\n")
        f.write("$" + perms + "['*']['edit'] = false;\n")
        f.write("$" + perms + "['*']['read'] = false;\n")

    print('Added Settings')

def get_inputs_dict_from_html(text):
    soup = bs4.BeautifulSoup(text, 'html.parser')
    inputs = soup.select('form input')

    filled = {}
    for i in inputs:
        if i.get('name', None) is None or i.get('value', None) is None:
            continue
        filled[i.get('name')] = i.get('Value')
    
    return filled

def language_page(session, get_url, post_url=None):
    filled = get_inputs_dict_from_html(session.get(get_url).text)

    filled['uselang'] = 'en'
    filled['ContLang'] = 'en'
    filled['submit-continue'] = filled.get('submit-continue', 'Continue →')
    filled['LanguageRequestTime'] = filled.get('LanguageRequestTime')

    post_url = post_url if post_url is not None else get_url

    return session.post(post_url, data=filled)

def welcome_page(session, response, get_url, post_url=None):
    # inputs = get_inputs_dict_from_html(response.text)
    post_url = post_url if post_url is not None else get_url
    return session.post(post_url, data={'submit-continue':'Continue →'})

def db_page(session, settings, response, get_url, post_url=None):
    post_url = post_url if post_url is not None else get_url

    submitted = {'DBType': 'mysql'}
    if 'host' in settings:
        submitted['mysql_wgDBserver'] = settings['host']

    if 'port' in settings:
        submitted['mysql_wgDBport'] = settings['port']

    if 'user' in settings:
        submitted['mysql__InstallUser'] = settings['user']

    if 'password' in settings:
        submitted['mysql__InstallPassword'] = settings['password']

    if 'database'  in settings:
        submitted['mysql_wgDBname'] = settings['database']

    submitted['mysql_wgDBprefix'] = 'prefix_'
    submitted['submit-continue'] = 'Continue →'
    
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    submitted['sqlite_wgSQLiteDataDir'] = root_dir

    submitted['sqlite_wgDBname'] = settings['database']

    return session.post(post_url, data=submitted)

def random_string(length=15):
    r, s = random, string
    return ''.join(r.choices(s.ascii_uppercase + s.digits, k=length))

def name_page(session, response, url):
    name_settings = {}
    name_settings[''] = ''
    name_settings['config_wgSitename'] = 'Contests'
    name_settings['config__NamespaceType'] = 'site-name'
    name_settings['config_wgMetaNamespace'] = 'MyWiki'
    name_settings['config__AdminName'] = 'Admin'
    name_settings['config__AdminPassword'] = random_string()
    name_settings['config__AdminPasswordConfirm'] = random_string()
    name_settings['config__AdminEmail'] = 'admin@example.com'
    name_settings['config__SkipOptional'] = 'skip'
    name_settings['submit-continue']: 'Continue →'

    return session.post(url, data=name_settings)
