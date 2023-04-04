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
        time.sleep(10)



def downloading(dict):
    if dict['status'] == 'downloading':
        print(f"Currently downloading..\nETA: {dict['eta']} second(s) @ {dict['speed']} bytes/s")
        time.sleep(0.5)
        os.system("cls")

def done(dict):
    if dict['status'] == "finished":
        print("Finished downloading, now postprocessing..")

def post_done(dict):
    if dict['status'] == "finished":
        print("Finished postprocessing!")



# Video & Audio options that are passed to the downloader. 
# Feel free to change the 'preferedformat' and 'preferredcodec' values according to the README.md
v_opts = {
    'format' : 'best',
    'logger' : Logger(),
    'progress_hooks' : [downloading, done],
    'postprocessor_hooks' : [post_done],
    'postprocessors' : [{
    'key' : 'FFmpegVideoConvertor',
    'preferedformat' : 'mp4',
    }],
}

a_opts = {
    'format' : 'bestaudio/best',
    'logger' : Logger(),
    'progress_hooks' : [downloading, done],
    'postprocessor_hooks' : [post_done],
    'postprocessors' : [{
    'key' : 'FFmpegExtractAudio',
    'preferredcodec' : 'mp3',
    'preferredquality' : '192',
    }],
}



while True:
    print("Hi! Please choose whether you want to download a video or an audio.\nAvailable options: audio/video")
    choice = input()
    if choice.lower() == "audio":
        print("Please paste a URL:")
        url = input()
        with yt_dlp.YoutubeDL(a_opts) as ytdl:
            ytdl.download(url)

    elif choice.lower() == "video":
        print("Please paste a url:")
        url = input()
        with yt_dlp.YoutubeDL(v_opts) as ytdl:
            ytdl.download(url)

    else:
        print("Please choose one of the available options.")

    time.sleep(1)
    os.system("cls")
    