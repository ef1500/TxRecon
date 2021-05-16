# -*- coding: utf-8 -*-

from termcolor import colored
import TxTriangulate as yuzu
import TxUsrFinder as mei
import TxThreader as peko
import argparse
import sys
import os

def printscreen():
    text = """
                     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡿⣛⣭⣭⣭⣿⣶⣶⣶⣶⣶⣯⣐⡯⣻⢿⣶⣾⣯⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿              _____      ____
                     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⢷⣪⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣶⣕⡯⡻⣿⣿⣷⣝⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿             |_   _|_  _|  _ \ ___  ___ ___  _ __
                     ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢏⣴⢿⣵⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣻⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣿⣷⡌⠻⣿⣿⣿⣿⣿⣿⣿               | | \ \/ / |_) / _ \/ __/ _ \|  _ \\
                     ⣿⣿⣿⣿⣿⣿⣿⣿⡿⡵⣵⣿⣽⣿⣿⣿⣯⣿⣯⣿⣿⣿⣿⣿⣹⣿⣯⣿⣿⣿⣿⣿⣿⡿⣿⣿⣷⠙⡄⣻⣿⣿⣦⢮⡻⣿⣿⣿⣿⣿               | |  >  <|  _ <  __/ (_| (_) | | | |
                     ⣿⣿⣿⣿⣿⣿⣿⣫⢎⣾⣿⣿⣿⣽⣿⣟⣼⣯⡿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⠘⡳⣯⣥⣤⣬⢿⣌⢿⣿⣿⣿               |_| /_/\_\_| \_\___|\___\___/|_| |_|
                     ⣿⣿⣿⣿⣿⡿⣳⣣⣿⣻⣿⣿⢻⣿⣿⢻⠿⣽⣻⣿⣿⣿⢇⡏⡏⣿⣿⣷⢿⣧⢿⣿⣿⣿⣷⣻⣿⡇⡇⢳⠛⣟⣋⣉⡜⣿⣧⣻⣿⣿    +======================================================+
                     ⣿⣿⣿⣿⡟⣼⣣⣿⣿⣿⣿⡿⣾⣿⣯⡟⢴⢷⣿⣿⣿⡟⣼⢱⢁⢹⢿⣿⣼⣿⣾⣿⣿⣾⣿⣿⣿⣧⢓⠈⡎⣿⠿⠿⠃⣿⣿⣷⣹⣿     Twitter Triangulator and Username searcher
                     ⣿⣿⣿⡿⣼⣯⣿⣿⣿⣿⣿⠃⣿⣿⢻⡏⣜⣾⣿⡿⡿⠘⡟⡞⣺⡜⢈⣿⣷⣿⡇⣿⣿⡿⣿⣧⣿⣿⠀⠀⡇⣿⣿⣿⠿⣿⣾⣿⢳⣹     Author: ef1500
                     ⣿⣿⣿⣹⣿⣿⣟⣿⣿⣿⡟⠀⣿⣿⣿⢠⢿⣿⡿⡿⢃⣼⠀⢰⣿⣣⠂⠹⣿⣿⡇⢹⣿⣧⣿⣿⣸⣿⢐⠀⡇⣷⣶⣶⡖⣿⣯⢿⡟⣯    +======================================================+
                     ⣿⣿⣧⡏⣿⣿⣿⣿⣿⣿⢁⠀⣿⣿⡯⢨⣿⡿⡽⣡⣧⢣⢈⣾⣿⣿⡄⠂⣹⣿⣇⢸⣿⣿⢹⣿⢹⣿⡄⠄⠻⣏⣉⣭⣅⣿⣿⡾⣿⣼
                     ⣿⣿⡘⣸⣿⣿⢸⣿⣿⡿⣾⡀⣿⣿⡇⢸⣟⠝⣠⡟⠮⠃⠮⠿⠿⡿⣷⡈⡐⣿⣿⢸⣿⣿⣼⣿⣼⣿⡇⠂⢃⣛⡛⡋⠸⣿⣿⣧⢻⣏
                     ⣿⢇⣿⢻⣿⣿⢸⣿⡟⢁⣿⡇⣿⣿⡧⠫⡞⣠⡕⢠⣞⣼⣿⣿⣿⠿⣿⣷⡀⢹⣿⠈⣿⣿⣿⣿⡏⣿⡇⠐⠐⢟⢔⠻⢗⢹⣿⣿⡌⢿
                     ⣏⣼⠸⣿⣿⣿⢸⣿⠹⢘⣻⣥⡿⠋⢀⡿⣱⢏⣴⣯⢎⠉⠀⠀⠀⠀⠀⠀⠀⢸⣿⢠⣿⣿⣿⣿⡇⣿⢃⣾⢟⠗⠁⠚⠓⠸⣿⣿⡇⡘
                     ⣶⡄⡇⣿⣿⣿⣼⣿⢂⣾⣿⡇⡞⠂⢹⢫⣳⣷⣿⣷⣴⠀⣴⣾⡀⠤⡈⠀⠀⢸⡏⢸⣿⣿⣿⣿⡇⣿⠨⣪⣶⣿⣿⠿⣿⣆⢸⣿⡇⣾
                     ⣿⣇⡇⢿⢿⣿⡏⡏⠠⠉⠒⠂⠀⠁⣆⣾⣿⣿⣿⣯⣷⣦⣿⣿⣃⣤⣤⣶⣿⣿⠃⣾⣿⣿⣿⣿⡇⡏⢸⡿⢋⣥⣶⣶⣤⡈⢸⣿⡇⢽
                     ⣿⣟⠀⠘⣿⣿⣇⠀⠀⢀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢨⡇⣟⣿⣿⣿⣿⡇⡇⢊⣴⣿⣿⣿⣿⣿⣷⢸⣿⡇⢾
                     ⣿⣧⣧⢀⢡⣿⣿⠘⡀⣻⡮⢀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣾⣷⣿⣿⣿⢸⣿⢹⠃⣾⣿⣿⣿⣿⣿⣿⣇⢸⣿⡇⣿
                     ⣿⣿⣿⡀⡆⠈⢿⡀⢧⣿⣿⣿⣿⣿⣿⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⢸⣿⣿⡏⣿⡟⡜⠐⣿⣿⣿⣿⣿⣿⢿⣾⣸⣿⣧⣿
                     ⣿⣿⢺⣧⡁⡄⡈⠃⠀⠊⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⢳⣿⣷⢅⠀⠙⠿⢿⠿⡛⣵⣿⡗⢽⣿⢻⣿
                     ⣿⢸⣸⡿⡇⡇⠇⣶⣌⡀⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣸⣿⡟⠰⠀⣨⣤⣶⡆⢣⣿⣿⢹⣸⣿⣿⣿
                     ⣿⢸⣽⣏⡇⣿⢀⢏⣿⡃⣌⢿⣿⣿⣿⣿⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿⣿⣧⣿⡿⠀⣀⠀⣿⣿⣿⠡⣸⣿⠏⡥⣿⣿⣿⣏
                     ⡏⢸⣿⣿⡇⣿⠸⢹⣿⡏⣽⢈⠻⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⣿⣿⣽⣿⣇⣼⣿⢐⣿⣿⡟⢰⣿⡟⣴⡸⣽⣿⡻⢱
                     ⡇⣸⡏⣯⣿⢿⡇⡌⣿⣷⢸⢸⣷⣌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢲⣿⣿⣿⡟⣹⣿⠏⣺⣿⣿⢱⣾⡿⢀⠟⢳⣿⠇⡱⣳
                     ⡇⣿⣧⠱⡎⡼⣷⢹⢺⣿⡀⡞⣿⣿⣷⠈⡛⠿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⢸⣟⣿⣯⢧⣿⠞⢰⣿⣿⢣⣳⣿⡜⠜⣢⡿⢃⠜⢹⣿
                     ⡇⡇⣿⡌⣿⠁⣿⡆⣧⠷⢦⠂⣿⣿⣿⣸⢿⡇⠈⡉⠉⢩⡄⡆⠀⠀⠀⠀⠀⣾⢻⣿⣉⢒⡟⢡⣿⡿⠃⣨⣏⠈⠀⡴⠋⢀⣱⡇⢸⣿"""
    text.encode("utf-8")
    colortext = colored(text, 'green')
    print(colortext)

def main():
    printscreen()
    parser = argparse.ArgumentParser() #start the argument parser
    parser.add_argument("t1", help="Target 1 - Should Be the username of a twitter user", type=str)
    parser.add_argument("t2", nargs='?', help="Target 2 - Should Be the username of a twitter user", type=str)
    parser.add_argument("-Mx", "--mutuals", action="store_true", help="Only Target Mutuals")
    parser.add_argument("-Tx", "--searchtarget", action="store_true", help="Use WhatsMyName to search for the targets specified")
    yuu = parser.parse_args()
    if yuu.mutuals:
        print("Mutual Flag set. Only targeting mutuals closest to the target")
        My = yuzu.GrabMx(yuu.t1, yuu.t2)
        Myy = list(dict.fromkeys(My))
        print("Reduced list: " + str(Myy))
        peko.ThreaderEngine(Myy)
    elif yuu.t2 and yuu.searchtarget:
        print("Searchtarget operator only takes 1 username!", 'green')
        exit()
    elif yuu.searchtarget:
        print("Searchtarget Flag Set. Only searching for the user specified")
        Mv = []
        Mv.append(str(yuu.t1))
        peko.ThreaderEngine(Mv)
    else:
        Mx = yuzu.GrabIDs(yuu.t1, yuu.t2)
        Mxy = list(dict.fromkeys(Mx))
        print("Reduced list: " + str(Mxy))
        #mei.StartUserLoc(Mxy)
        peko.ThreaderEngine(Mxy)

if __name__ == "__main__":
    main()
