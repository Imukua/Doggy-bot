
client_id = '94732c26a56f2266712b7f2b3bae0a7e8265ce0336d35b9a29ff686e72193c2c'
client_secret = '6fcdd80a3cbeb6dd637c4ee1ab803d6c5c785e894607e2d3b6027fc751de07a2'

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': client_id,
    'Authorization': f'Bearer {client_secret}'
}

url = 'https://api.trakt.tv/shows/{show_slug}/last_episode'


trakt_object = {
    'client_id': client_id,
    'client_secret': client_secret,
    'headers': headers,
    'url': url
}
class TVShow:
    def __init__(self, name, season, episode, title, watched):
        self.name = name
        self.season = season
        self.episode = episode
        self.title = title
        self.watched = watched

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], row[3], row[4])

    @classmethod
    def from_table(cls, table):
        shows = {}
        for row in table:
            show = cls.from_row(row)
            shows[show.name] = show
        return shows
