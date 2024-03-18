import sys
import utils.json_fns as fns

if len(sys.argv)>1:
    operation = sys.argv[1:][0]
    match operation:
        case 'read':
            fns.read_from_json()
        case 'write':
            msg = input("what is your msg? ")
            if msg:
                err_writing = True
                while err_writing == True: 
                    try:
                        fns.write_to_json(msg)
                        err_writing = False
                    except Exception as e :
                        err_writing = True
else:
    print("no operator")
