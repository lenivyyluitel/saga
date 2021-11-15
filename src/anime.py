import requests
from jikanpy import Jikan

class finder:
    def finder(self, name_):
        global result
        jikan = Jikan()

        info = jikan.search(search_type='anime', query=name_)
        get = info['results'][0]
        image = (info['results'][0]['image_url'])

        title = (get['title'])
        try:
            airing = (get['airing'])
        except Exception:
            airing = None
        typee = (get['type'])
        try:
            episodes = (get['episodes'])
        except Exception:
            episodes = None
        score = (get['score'])
        start_date = (get['start_date'])
        start_date = start_date.replace('T00:00:00+00:00', '').replace("'", '')
        end_date = (get['end_date'])
        end_date = end_date.replace('T00:00:00+00:00', '').replace("'", '')
        members = (get['members'])
        try:
            rated = (get['rated'])
        except Exception:
            rated = None
        
        image = (f'''{image}''')
        result = (
            f'''Title: {title}
Episodes: {episodes}
Airing: {airing}
From: {start_date} to {end_date}
Type: {typee}
Score: {score}
Members: {members}
Rated: {rated}
''')
        result2 = image
        self.result2 = result2
        self.result = result
