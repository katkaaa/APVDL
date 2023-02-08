import yt_dlp
import time
import os 


# Logger, pretty much filtering what to print to avoid cluttering in the console
class Logger(object):
    def debug(self, msg):
        pass
    
    def warning(self, msg):
        pass
    
    def error(self, msg):
        print(msg)

def downloading(dict):
    if dict['status'] == 'downloading':
        print(f"Currently downloading..\nETA: {dict['eta']} second(s) @ {round(dict['speed'] / 1000, 2)} kbps")

def done(dict):
    if dict['status'] == "finished":
        print("Finished downloading, now postprocessing..")

def post_done(dict):
    if dict['status'] == "finished":
        print("Finished postprocessing!")




