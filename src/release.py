import requests
from datetime import datetime

class release:
  def release(self, release):
    query = '''
    query ($search: String){
      Media (search: $search, type: ANIME) {
        title {
          romaji
          english
          native
        }   
        coverImage {
          medium
          }
        nextAiringEpisode{episode}
        airingSchedule{nodes{airingAt}}  }
    }
    '''

    variables = {
        'search': f"{release}"
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    cover = (data['data']['Media']['coverImage']['medium'])
    native = (data['data']['Media']['title']['native'])
    romaji = (data['data']['Media']['title']['romaji'])
    nextAiring = (data['data']['Media']['nextAiringEpisode']['episode'])
    episode = (data['data']['Media']['airingSchedule']['nodes'][0]['airingAt'])
    animeTime = int(episode)
    episode_date = (datetime.utcfromtimestamp(animeTime).strftime('%Y-%m-%d'))
    episode_time = (datetime.utcfromtimestamp(animeTime).strftime('%H:%M'))
    airing = (f"{native}\n{romaji}\nupcoming episode: {nextAiring}\nrelease date: {episode_date}\nrelease time: {episode_time}")
    self.airing = airing
    self.cover = cover