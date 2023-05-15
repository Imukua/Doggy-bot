from myobjects import trakt_object as tobj, TVShow
import requests
from tabulate import tabulate

def elatest_episode():
    myshows = ['the-blacklist','power-book-ii-ghost','demon-slayer-kimetsu-no-yaiba','rabbit-hole']
    myshowsurl = {}
    for show in myshows:
        tobjcp = tobj.copy()
        myshowsurl[show] = tobjcp['url'].format(show_slug = show)
    
    myshowsurl['watched'] = False
    table = []
    for show in myshowsurl:
        if show != 'watched':
            response = requests.get(myshowsurl[show], headers=tobj['headers'])
            if response.status_code == 200:
                data = response.json() #data contains a single shows info 
                row = []
                row.append(show)
                row.append(data['season'])
                row.append(data['number'])
                row.append(data['title'])
                row.append(myshowsurl['watched'])
                table.append(row)

            else:
                if response.status_code == 404:
                    print(f"Show: {show} not found")
                if response.status_code == 204:
                    print()
                    print(f"Show: {show} has no episodes left this season\n")
                else:
                    print(response.status_code)
    
    return TVShow.from_table(table)

if __name__ == "__main__":
    shows_data = elatest_episode()
    print("{} {} {} {}".format(shows_data['the-blacklist'].name, shows_data['the-blacklist'].season,
                               shows_data['the-blacklist'].episode, shows_data['the-blacklist'].title))