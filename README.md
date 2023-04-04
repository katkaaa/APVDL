# APVDL - Another python video downloader
This tool allows you to download videos (or audio) from mainly youtube, although it should work on all of the [supported websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md). 

Take a look at the [tested websites](#tested-websites).

This program uses [YT-DLP](https://github.com/yt-dlp/yt-dlp) and [FFmpeg](https://www.ffmpeg.org).

# Installation
You will need:
 - [Python 3.10+](https://www.python.org/downloads/)
 - [FFmpeg](https://www.ffmpeg.org/download.html) (make sure it's in **PATH**)

In CMD (as administrator), run the following command:

``cd <the path you downloaded this repo to>``

and then:

``python3 pip install -r requirements.txt``

This will ensure you have all the dependencies required for this program to work.


# How to use?
In CMD (as administrator), run the following command:

``cd <the path you downloaded this repo to>``

and then:

``py main.py``


# Tested websites
 - youtube.com - ✅ 
 - video.aktualne.cz - ✅
 - reddit.com - ✅, just make sure to right click the video and click copy video address
 - seznamzpravy.cz - ❌
 - stream.cz - ✅
 - twitter.com - ✅, but the tweet **cannot** contain any type of quotes
 - ceskatelevize.cz - ❌, throws 404, will probably be fixed soon by the yt-dlp devs


# Issues
As of writing this README.md, it seems that everything is working correctly. Please submit an issue if you find one.


# Getting help
In case something doesn't work:
 - Make sure you have everything set up correctly
 - Try updating the yt-dlp package using:
    ``python3 pip uninstall yt-dlp`` & ``python3 pip install yt-dlp``
 - If neither of these work, **submit an issue**.


# To do
 - Fix that awful speed display


## Note
This program was created solely for **educational purposes**. 
