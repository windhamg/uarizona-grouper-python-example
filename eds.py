import os
from ldap3 import Server, Connection, ALL, LEVEL

def get_uaid(netid):
    # connect and bind to EDS LDAP directory
    eds_server = Server(os.environ['EDS_URL'], get_info=ALL)
    eds_conn = Connection(
        eds_server,
        f"uid={os.environ['EDS_USERNAME']},ou=app users,{os.environ['EDS_BASE_DN']}",
        os.environ['EDS_PASSWORD'],
        auto_bind=True,
        raise_exceptions=True)

    # execute search
    eds_conn.search(
        f"ou=people,{os.environ['EDS_BASE_DN']}",
        f"(&(objectclass=arizonaeduperson)(uid={netid}))",
        search_scope=LEVEL,
        attributes=['uaid']
    )

    # get result
    e = None
    if len(eds_conn.entries):
        e = eds_conn.entries[0]

    eds_conn.unbind()

    # return EDS attrs
    return e['uaid'][0] if e else None