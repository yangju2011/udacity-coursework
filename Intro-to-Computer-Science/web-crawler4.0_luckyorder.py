#######################################
# This is 4.0 version of Web Crawler. #
# --------- Ju Yang 2016.08.09. ------#
#######################################

'''if use the urllib function, to get data from the internet, will be slower than cache function
'''

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
        if url: # this would avoid duplicate links, also make sure url is not None
            if url not in links:  # remove None from the output
                links.append(url)
                page = page[end_quote+1:]
        else:
            break # add this break line
    return links


def add_to_index(index,keyword,url): #index is a list [[keyword, [url1,url2],[kw2,[]]
    if keyword in index: # check if keyword is in index
    # if index[keyword]: 
        if url not in index[keyword]: # not to repeat 
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

def lucky_search(index, ranks, keyword):
    if keyword not in index: #look up page function
        return None
    else:
        urls=index[keyword] #return list of [url]
        keyword_ranks=[]
        for url in urls:
            rank=ranks[url] #assumr first page is the best page, then iterate all other urls ranks[page]<ranks[url], return url
            keyword_ranks.append([url,rank])
        max_rank=keyword_ranks[0][1]
        max_url=keyword_ranks[0][0] #assume the max page is the first page
        for e in keyword_ranks:
            if e[1]>=max_rank:
                max_rank=e[1]
                max_url=e[0]
        return max_url

def ordered_search(index, ranks, keyword):
    if keyword not in index:
        return None
    else:
        urls=index[keyword] 
        if len(urls)==1:
            return urls # urls is a list in index dict
        else:
            url_ranks={}
            rank_order=[]
            url_sort=[]
            for url in urls:
                rank=ranks[url] 
                url_ranks[rank]=url
                rank_order.append(rank)
            rank_sort=quicksort(rank_order)
            for e in rank_sort:
                urlsort=url_ranks[e]
                url_sort.append(urlsort)
            return url_sort # which is ordered outlinks with value by rank number 

# recursive sorting function               
def quicksort(p): 
    if p==[] or len(p)==1:
        return p
    else:
        pivot=[p[0]]
        p_small=[]
        p_big=[]
        for e in p[1:]:
            if e <= pivot[0]:
                p_small.append(e)
            else:
                p_big.append(e)
        return quicksort(p_big)+pivot+quicksort(p_small) 

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

ranks = compute_ranks(10,1,0.8,graph)
print ranks

