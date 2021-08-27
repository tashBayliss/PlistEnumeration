import r2pipe
import os

def analysis(filename):
    r = r2pipe.open(filename)

    #print(r.cmd('ia ~canary'))

    r.cmd('aaa')
    print(r.cmd('afl'))
    print(r.cmd('pdf @ main'))

    # reopen binary at main
    r.cmd('ood')
    # break at main
    r.cmd('db main')
    #print
    print(r.cmd('dc'))
    
    

    r.quit()

def checkPath():
    fileName=os.path.expanduser(input("\nEnter binary file path: "))
    #~/Documents/Project/Payload/DVIA-v2.app/DVIA-v2

    if (os.path.exists(fileName)):
        analysis(fileName)

    else:
        print("Please enter a valid file path")
        checkPath()

def main():
    print("""\
  ____  _                                               _           _     
 |  _ \(_)                            /\               | |         (_)    
 | |_) |_ _ __   __ _ _ __ _   _     /  \   _ __   __ _| |_   _ ___ _ ___ 
 |  _ <| | '_ \ / _` | '__| | | |   / /\ \ | '_ \ / _` | | | | / __| / __|
 | |_) | | | | | (_| | |  | |_| |  / ____ \| | | | (_| | | |_| \__ | \__ \\
 |____/|_|_| |_|\__,_|_|   \__, | /_/    \_|_| |_|\__,_|_|\__, |___|_|___/
                            __/ |                          __/ |          
                           |___/                          |___/                   
""")
    print("Binary Analysis Tool")
    checkPath()

if __name__ == '__main__':
    main()
