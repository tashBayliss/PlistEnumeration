import os
import plistlib
import warnings
import zipfile

warnings.filterwarnings("ignore", category=DeprecationWarning)

fakeFile = {'NSAppTransportSecurity': {'NSAllowsArbitraryLoads': True, 'TestValue': False}, 'NSCameraUsageDescription': 'To demonstrate the misuse of Camera, please grant it permission once.'}

insecureKeys = {
    "NSAppTransportSecurity": {
        "NSAllowsArbitraryLoads": True,
        "TestKey": True,
        },
    "NSAllowsLoadsForMedia": True,
    "NSAllowsArbitaryLoadsInWebContent": True,
    "NSAllowsLocalNetworking": True,
    "NSAllowsInsecureHTTPLoads": True,
    "NSExceptionMinimumTLSVersion": "TLSv1.1",
    }

#improve this function efficiency 
def search(fileName):
    pl = plistlib.readPlist(fileName)
    count = 0

    for key in insecureKeys.keys():
        if (key in pl):
            
            # check for match
            if (insecureKeys[key] == pl[key]):
                    print("Key ", key, " is vulnerable with value: ", pl[key])
                    count = count + 1

            # check nested dictionary for match
            elif (type(insecureKeys[key]) is dict):
                try:
                    for i in insecureKeys[key].keys():
                        if (type(pl[key]) is dict):
                            for j in pl[key].keys():
                                if (insecureKeys[key][i] == pl[key][j]):
                                    print("Key ", key, " is vulnerable with value: ", pl[key][i], "- File:", os.path.basename(os.path.dirname(fileName)),"/Info.plist")
                                    count = count + 1

                except KeyError:
                    continue

            # if no match, continue to the next for
            else:
                continue

            print()

        else:
            continue

    if(count == 0):
        print("No security vulnerabilities discovered in", os.path.basename(os.path.dirname(fileName)),"/Info.plist")

def checkPath(fileName, option):
    fileName=os.path.expanduser(fileName)
    
    if (os.path.exists(fileName)):
        if(option == 1):
            # Check that file path is actually Info.plist
            if (os.path.basename(fileName) == "Info.plist"):
                search(fileName)

            else:
                print("please select a valid plist file")
                options()
            
        if(option == 2):
            # Extract ipa to current directory
            with zipfile.ZipFile(fileName, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(fileName))

            # Create path link to extracted ipa
            newPath = os.path.expanduser(os.path.dirname(fileName) + "/Payload")

            infoPaths = []

            for root, dir, files in os.walk(newPath):
                if "Info.plist" in files:
                    infoPaths.append(os.path.join(root, "Info.plist"))
            
            for i in range (0, len(infoPaths)):
                search(infoPaths[i])
              
    else:
        print("%s does not exist, so can't be read." % fileName, " Please Try again")
        options()

def options():
    print("\nSelect an option:\n1. Enter Info.plist file location\n2. Enter .ipa file location to extract and locate Info.plist\n3. Quit")
    option = int(input("Option: "))

    try:
        if (option == 1):
            fileName=os.path.expanduser(input("\nEnter Info.plist file path: "))
            #~/Documents/Project/DVIA-v2-swift/Payload/DVIA-v2.app/AntiAntiHookingDebugging.storyboardc/Info.plist
            #~/Documents/Project/DVIA-v2-swift/Payload/DVIA-v2.app/Info.plist
            print()
            checkPath(fileName, option)

        elif (option == 2):    
            fileName=os.path.expanduser(input("\nEnter ipa file path: "))
            #~/Documents/Project/DVIA-v2-swift.ipa
            print()
            checkPath(fileName, option)

        elif (option == 3):
            exit()

        else:
            print("please select a valid option")
            options()

    except ValueError:
        print("please select a valid option")
        options()
        
def main():
    print("""\

  _____  _ _     _     ______                                      _   _             
 |  __ \| (_)   | |   |  ____|                                    | | (_)            
 | |__) | |_ ___| |_  | |__   _ __  _   _ _ __ ___   ___ _ __ __ _| |_ _  ___  _ __  
 |  ___/| | / __| __| |  __| | '_ \| | | | '_ ` _ \ / _ \ '__/ _` | __| |/ _ \| '_ \ 
 | |    | | \__ \ |_  | |____| | | | |_| | | | | | |  __/ | | (_| | |_| | (_) | | | |
 |_|    |_|_|___/\__| |______|_| |_|\__,_|_| |_| |_|\___|_|  \__,_|\__|_|\___/|_| |_|
                                                                                     
                                                                                     
""")
    print("Plist Enumeration Tool")

    while (True):
        options()
    
if __name__ == '__main__':
    main()
