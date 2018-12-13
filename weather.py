import feedparser as feed
url =  "http://weather.livedoor.com/forecast/rss/area/130010.xml"
weather = feed.parse(url)
for entry in weather.entries:
    print(entry.title)
    print(entry.link)
    
