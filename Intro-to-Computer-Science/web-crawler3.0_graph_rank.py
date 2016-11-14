#######################################
# This is 3.0 version of Web Crawler. #
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
            if url:  # remove None from the output
                links.append(url)
                page = page[end_quote+1:]
        else:
            break # add this break line
    return links


def add_to_index(index,keyword,url): #index is a list [[keyword, [url1,url2],[kw2,[]]
    if keyword in index: # check if keyword is in index
    # if index[keyword]: 
        if url not in index[keyword]:
            index[keyword].append(url)
    else:
        index[keyword] = [url] #directly create new index, it is a list
#   need not to return index

def add_page_to_index(index,url):
    page = get_page(url)
    keywords = page.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)
#   need not to return index

def lookup (index,keyword):
    if keyword in index: # index is {}
        return index[keyword]
    return None
# if keyword not in index, return None

def compute_ranks(loops,intial,d,graph): # a graph has link as key, and outlinks as value, d as damping factor, rank is a {url:rank} 
    ranks = {}
    
    for page in graph:
        ranks[page] = intial

    for i in range(0,loops): # t here is not a time number, but the repeat number, could be writter as loops # given each page an intial rank > 0
        newranks = {}
        
        for page in graph:
            newrank=(1-d)/len(graph) # npages
            
            for node in graph:
                if page in graph[node]:
                    # divided by total number of outlinks
                    newrank = newrank+ d*ranks[node]/len(graph[node])
            newranks[page] = newrank #if no input link, then is 1-d/N
        ranks = newranks
    return ranks

def crawl_web(seed_url): # seed is the url of the seeding page
    tocrawl = [seed_url]
    crawled = []
    graph = {}
    index = {}
    while tocrawl:
        url = tocrawl.pop()
        if url not in crawled: # make sure not to repeat crawling 
            add_page_to_index(index,url) # this is an operation, not need to return anything
            outlinks = get_all_links(url) # store link information in graph{url:[outlinks]}
            graph[url] = outlinks # right after outlinks are calculated
            for link in outlinks:
                if link not in tocrawl: 
                    tocrawl.append(link)
        crawled.append(url)
    return index,graph
# if no outlinks, return None

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
# print get_all_links('http://udacity.com/cs101x/urank/index.html')
loops = 10
d = 0.8
intial = 1
ranks = compute_ranks(10,1,0.8,graph) 
print ranks
'''
{'http://udacity.com/cs101x/urank/kathleen.html': 0.11661866666666663, 'http://udacity.com/cs101x/urank/zinc.html': 0.038666666666666655, 'http://udacity.com/cs101x/urank/hummus.html': 0.038666666666666655, 'http://udacity.com/cs101x/urank/arsenic.html': 0.054133333333333325, 'http://udacity.com/cs101x/urank/index.html': 0.033333333333333326, 'http://udacity.com/cs101x/urank/nickel.html': 0.09743999999999997}
'''
