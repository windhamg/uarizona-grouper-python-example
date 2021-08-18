import os
import requests
import logging

def add_member(uaid, group):
    """ 
    Add member to Grouper group

    Args:
        uaid: (string): UAID of member to add
        group: (string): group to add member to        
    Returns: 
        True if member added to group, False otherwise.
    """

    headers = {'Content-Type': 'text/x-json; charset=UTF-8'}
    payload = {
        "WsRestAddMemberRequest": {
            "subjectLookups": [{"subjectId": uaid}],
            "replaceAllExisting": "F"
        }
    }
    try:
        r = requests.put(
            f"{os.environ['GROUPER_BASE_URL']}/groups/{group}/members",
            headers=headers,
            json=payload,
            auth=(
                os.environ['EDS_USERNAME'],
                os.environ['EDS_PASSWORD']
            )
        )
        if r.status_code in [200, 201] and 'X-Grouper-resultCode' in r.headers and r.headers['X-Grouper-resultCode'] in ['SUCCESS', 'SUCCESS_ALREADY_EXISTED']:
            return True
        else:
            logging.error(f"Group add member error: member = {uaid}, error = {r.headers['X-Grouper-resultCode']}, detail = {r.json()}")
    except Exception as e:
        logging.error(f"Group add member exception: member = {uaid}, exception = {e}")
    return False


def delete_member(uaid, group):
    """ 
    Delete member from Grouper group

    Args:
        uaid: (string): UAID of member to delete
        group: (string): group to remove member from        
    Returns: 
        True if member deleted from group, False otherwise.
    """

    headers = {'Content-Type': 'text/x-json; charset=UTF-8'}
    payload = {
        "WsRestDeleteMemberRequest": {
            "subjectLookups": [{"subjectId": uaid}]
        }
    }
    try:
        r = requests.put(
            f"{os.environ['GROUPER_BASE_URL']}/groups/{group}/members",
            headers=headers,
            json=payload,
            auth=(
                os.environ['EDS_USERNAME'],
                os.environ['EDS_PASSWORD']
            )
        )
        if r.status_code == 200 and 'X-Grouper-resultCode' in r.headers and r.headers['X-Grouper-resultCode'] == 'SUCCESS':
            return True
        else:
            logging.error(f"Group delete member error: member = {uaid}, error = {r.headers['X-Grouper-resultCode']}, detail = {r.json()}")
    except Exception as e:
        logging.error(f"Group delete member exception: member = {uaid}, exception = {e}")
    return False