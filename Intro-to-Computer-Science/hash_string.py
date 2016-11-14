# better hash function

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def bad_hash_string(keyword, bucket):
    return ord(keyword[0])% bucket

def hash_string(keyword, bucket):
    suml = 0
    for l in keyword:
        suml = suml + ord(l)
    return suml % bucket 

# print hash_string('au', 12)

def test_hash_function(func,keys,bucket):
    results = [0]*bucket #[0,0,0,0...] for counts
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w,bucket)
            results[hv] += 1
            keys_used.append(w)
    return results # counts for each bucket

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
counts = test_hash_function(bad_hash_string,words,12)
# print counts
# [730, 1541, 1055, 1752, 1784, 839, 1452, 2074, 1409, 754, 924, 899]
# counts = test_hash_function(hash_string,words,12)
# print counts
# [1368, 1268, 1273, 1279, 1284, 1245, 1207, 1228, 1281, 1232, 1233, 1315]
counts = test_hash_function(hash_string,words,100)

import matplotlib.pyplot as plt # download from cmd using pip install 
import plotly.plotly as py

N = 100
x = range(N)
width = 1/1.5
plt.bar(x,counts,width,color='blue')

fig = plt.gcf()
plot_url = py.plot_mpl(fig,filename = 'hash string')
