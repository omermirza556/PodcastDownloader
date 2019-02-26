import feedparser, os, sys, subprocess
import argparse
import urllib.request

# open file makes the file play on the local computer
# *CITED FROM THE HOMEWORK INSTRUCTIONS*
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# get_url gets the url for the podcast
def get_Url(parsed_feed, n):
    return parsed_feed['entries'][n]['media_content'][0]['url']

# gets title of the feed
def get_title(parsed_feed):
    return parsed_feed['feed']['title']

# gets podcasts title
def get_podcast_title(parsed_feed, n):
    return parsed_feed['entries'][n]['title']

# gets multiple urls for the amount chosen
def get_mult_url(parsed_feed, n):
    url = []
    for i in range(0, n):
        url.append(get_Url(parsed_feed, i))
    return url

# gets summary of the podcast
def get_sumary(parsed_feed, n):
    return parsed_feed['entries'][n]['subtitle']

# does everything
def do_everything(removeSummary=False, it=0, choose=0, feed='http://atp.fm/episodes?format=rss'):
    choices = get_mult_url(feed, it)
    counter = 0

    for element in choices:
        if (removeSummary):
            print('******************' + '\n')
            the_title = (str(get_podcast_title(feed, counter)))
            print(the_title)
            print(element + '\n' + get_title(feed) + '\n' + get_sumary(feed, counter))
            counter += 1
        else:
            print('******************' + '\n')
            the_title = (str(get_podcast_title(feed, counter)))
            print(the_title)
            print(element + '\n' + get_title(feed))
            counter += 1
    chosen_podcast = get_Url(feed, choose)
    the_title = (str(get_podcast_title(feed, choose))) + '.mp3'
    urllib.request.urlretrieve(chosen_podcast, the_title)
    open_file(the_title)


def Main():
    parser = argparse.ArgumentParser(description='Allows you to download a podcast then play')
    parser.add_argument('-s', '--summary', type=bool, help='Remove podcast summary')
    parser.add_argument('-n', '--number', type=int, help='number of podcasts you wish to display')
    parser.add_argument('-p', '--choose', type=int, help='number of the podcast app you wish to play')
    parser.add_argument('-f', "--feed", type=str, help='feed to enter')
    args = parser.parse_args()

    do_everything(args.summary, args.number, args.choose, feedparser.parse(args.feed))


if __name__ == '__main__':
    Main()
