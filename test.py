import re

regex = r"database ['\"](.*)['\"]"

# test_str = "InternalError('(pymysql.err.InternalError) (1049, \"Unknown database \\'electora\\'\")',)"
test_str = """OperationalError('(psycopg2.OperationalError) FATAL:  database "electora" does not exist\n',)"""

matches = re.search(regex, test_str, re.MULTILINE)

if matches:
    print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
    print(matches.group(1))
    # for groupNum in range(0, len(matches.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))
