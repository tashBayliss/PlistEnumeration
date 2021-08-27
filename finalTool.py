import plistTool
import binaryAnalysis

def options():
    print("Select an option:")
    print("1. Plist Enumeration")
    print("2. Analyse binary file")
    print("3. Quit")

    option = int(input("Option: "))

    if (option == 1):
        plistTool.main()

    elif (option == 2):
        binaryAnalysis.main()

    elif (option == 3):
        exit()

    else:
        print("Please enter a valid option")

def main():
    print("""\
  _____ ____   _____   _______          _ _  ___ _   
 |_   _/ __ \ / ____| |__   __|        | | |/ (_) |  
   | || |  | | (___      | | ___   ___ | | ' / _| |_ 
   | || |  | |\___ \     | |/ _ \ / _ \| |  < | | __|
  _| || |__| |____) |    | | (_) | (_) | | . \| | |_ 
 |_____\____/|_____/     |_|\___/ \___/|_|_|\_\_|\__|
                                                     
""")
    
    print("IOS Toolkit")
    options()

if __name__ == '__main__':
    main()
