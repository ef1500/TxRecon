# TxThreader.py
# Multithreader for the twitter triangulator.
# Written by ef1500

import threading
import subprocess
import os

class Tx_thread (threading.Thread):
    def __init__(self, user, outputfile):
        threading.Thread.__init__(self)
        self.user = user
        self.outputfile = outputfile
    def run(self):
        print("Starting Thread on " + str(self.user))
        if os.name == 'nt':
            subprocess.run("python3 web_accounts_list_checker.py -u " + str(self.user) +" -of " + str(self.outputfile))
        else:
            os.system("python3 web_accounts_list_checker.py -u " + str(self.user) +" -of " + str(self.outputfile))

def ThreaderEngine(list):
    for user in list:
        pekora = Tx_thread(user, "tmp.txt")
        pekora.start()