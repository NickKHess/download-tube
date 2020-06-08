import argparse
import os

import youtube_dl

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python YouTube downloader for the command line')
    parser.add_argument('url', help='Video URL')
    parser.add_argument('-p', '--path', help='Path to download the file to (not including filename)')
    args = parser.parse_args()

    path = args.path
    if path is None:
        # Put the download into the current working directory
        path = os.getcwd()

    if os.path.isdir(path):
        path = path + os.path.sep + '%(title)s.%(ext)s'
    elif os.path.isfile(path):
        print('-p argument must not include filename!')
        exit()

    options = {'outtmpl': path}
    with youtube_dl.YoutubeDL(options) as ytdl:
        result = ytdl.download([args.url])


