import pyshorteners

def short_url(url):
    shortener = pyshorteners.Shortener()
    a = shortener.tinyurl.short(url)
    return a

url_data = "https://www.linkedin.com/in/geetavarshiny"
print(short_url(url_data))