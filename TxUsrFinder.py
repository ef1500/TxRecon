# UsrEngine
# Written By ef1500

import webbrowser

link = "https://whatsmyname.app/?q="
chromeDir = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
def StartUserLoc(users):
    # Startup a bunch of terminals for each user
    #"C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
    for ixer in users:
        webbrowser.get(chromeDir).open(str(link + ixer))
        print("Opening " + str(link + ixer))
