import sys
import utils.json_fns as fns

if len(sys.argv)>1:
    operation = sys.argv[1:][0]
    match operation:
        case 'read':
            fns.read_from_json()
else:
    print("no operator")
