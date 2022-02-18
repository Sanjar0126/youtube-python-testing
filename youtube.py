from __future__ import unicode_literals
import json
import yt_dlp
import logging

logging.basicConfig(format='%(message)s', encoding='utf-8', level=logging.DEBUG)

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        logging.info('Done downloading, now converting ...')
        

        
def function2(movie_id, name):
    if movie_id == "" or movie_id is None:
        return
    
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'final_ext': 'mp4',
        'outtmpl': "./output/" + name + ".%(ext)s",
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + movie_id])
        

URL = ""

error_links = []

file = open('movie.v2.json')

data = json.load(file)

file.close()

seen = set()
error = []

def download():
    for i, item in enumerate(data):
        logging.info('file ->  ' + item['slug'])
        for trailer in item['trailers']:
            try:
                function2(trailer['file_id'], item['slug'])
                seen.add(trailer['file_id'])
            except Exception as e:
                logging.error("error ->  " + trailer['file_id'] +  ' -> ' + str(e))
                error.append({"file_id": trailer['file_id'], "slug": item['slug'], "error": str(e)})
                continue
        if i == 4:
            break
            
    with open('errors.json', 'w', encoding='utf-8') as f:
        json.dump(error, f, ensure_ascii=False, indent=4)
        
download()