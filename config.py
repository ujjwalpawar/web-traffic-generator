MAX_DEPTH = 100  # maximum click depth
MIN_DEPTH = 50 # minimum click depth
MAX_WAIT = 1  # maximum amount of time to wait between HTTP requests
MIN_WAIT = 0  # minimum amount of time allowed between HTTP requests
DEBUG = True  # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#ROOT_URLS = ["https:///digg.com/"]

ROOT_URLS = [
	"http://www.cnn.com",
	"https://en.wikipedia.org/wiki/Main_Page",
	"https://austin.craigslist.org/",
        "https://www.bing.com/news/",
        "https://www.bbc.co.uk/news",
        "https://news.sky.com/uk",
        "https://www.dailymail.co.uk/news/index.html",
        "https://www.theguardian.com/tone/news",
        "https://news.ycombinator.com/",
        "https://www.reddit.com",

	]


#        "https://en.wikipedia.org/wiki/Main_Page",
#        "https://austin.craigslist.org/"
# items can be a URL "https://t.co" or simple string to check for "amazon"
blacklist = [
	"https://t.co", 
	"t.umblr.com", 
	"messenger.com", 
	"itunes.apple.com", 
	"l.facebook.com", 
	"bit.ly", 
	"mediawiki", 
	".css", 
	".ico", 
	".xml", 
	"intent/tweet", 
	"twitter.com/share", 
	"signup", 
	"login", 
	"dialog/feed?", 
	".png", 
	".jpg", 
	".json", 
	".svg", 
	".gif", 
	"zendesk",
	"clickserve"
	]  

# must use a valid user agent or sites will hate you
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
