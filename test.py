import sys
import grouper
import eds
from dotenv import load_dotenv

load_dotenv()

if len(sys.argv) != 4 or sys.argv[1] not in ['ADD', 'DEL']:
    print(f"Usage: {sys.argv[0]} <ADD|DEL> <netid> <group>", file=sys.stderr)
    exit(1)
op, netid, grp = sys.argv[1:]
uaid = eds.get_uaid(netid)
if uaid:
    if op == 'ADD':
        if grouper.add_member(uaid, grp):
            print(f"Successfully added {uaid} to group {grp}")
    else:
        if grouper.delete_member(uaid, grp):
            print(f"Successfully deleted {uaid} from group {grp}")
else:
    print(f"Error: {netid} not found in EDS", file=sys.stderr)
