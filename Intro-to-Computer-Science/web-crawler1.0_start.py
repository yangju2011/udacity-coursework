#######################################
# This is 1.0 version of Web Crawler. #
# --------- Ju Yang 2016.08.08. ------#
#######################################

def get_page(url):
    try:
        import urllib
        page = urllib.urlopen(url).read()
        return page
    except:
        return ''

def get_next_link(page):
    start_mark = page.find('<a href=')
    if start_mark == -1:
        return None, 0
    else: 
        start_quote = page.find('"',start_mark)
        end_quote = page.find('"',start_quote+1)
        url = page[start_quote+1:end_quote] # use : for range
        return url, end_quote

def get_all_links(url): # page is the content
    page = get_page(url)
    links = []
    while page:
        url, end_quote = get_next_link(page)
        if url not in links: # this would avoid duplicate links, also make sure url is not None
            links.append(url)
            page = page[end_quote+1:]
        else:
            break # add this break line
    return links


def add_to_index(index,keyword,url): #index is a list [[keyword, [url1,url2],[kw2,[]]
    for e in index:
        if keyword == e[0]:
            if url not in e[1]:
                e[1].append(url)
    index.append([keyword,[url]])
#   need not to return index

def add_page_to_index(index,url):
    page = get_page(url)
    keywords = page.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)
#   need not to return index
    

def lookup (index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return None
# if keyword not in index, return None

def crawl_web(seed_url): # seed is the url of the seeding page
    tocrawl = [seed_url]
    crawled = []
    index = []
    while tocrawl:
        url = tocrawl.pop()
        if url not in crawled: # make sure not to repeat crawling 
            add_page_to_index(index,url) # this is an operation, not need to return anything
            new_urls = get_all_links(url)
            for e in new_urls:
                if e not in tocrawl: 
                    tocrawl.append(e)
        crawled.append(url)
    return index,crawled

print crawl_web("https://www.udacity.com/cs101x/urank/index.html")
