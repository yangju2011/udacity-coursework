def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

# a try block, if not work, Error or return empty string
