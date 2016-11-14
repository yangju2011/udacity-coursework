# make hast table

def make_hashtable(nbuckets):
    table = []
    for i in range(nbuckets):
        table.append([])
    return table

def hash_string(keyword, bucket):
    suml = 0
    for l in keyword:
        suml = suml + ord(l)
    return suml % bucket 
# index of bucket, 'b'/12 -->2

# print make_hashtable(3)
# [[], [], []]
# [[[k1,v1],[k2,v2]],[[k3,v3]],[[k4,v4],[k5,v5]]..[],[],[]...]
# each k is assigned to bucket depending on sum(k)%bucket_size (0:bucket-1)

# print [[]]*3
# although results are the sam,e the latter one is incorrent, it means repeat the value in each bucket

def hashtable_get_bucket(hashtable,keyword): #return the whole bucket, which contains other keywords as well
    hash_index = hash_string(keyword,len(hashtable)) #bucket = len(hashtable)
    return hashtable[hash_index]
    
    
table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
# [['Bill', 17], ['Zoe', 14]]


# operations on hashtable
# add, update, lookup

def hashtable_add(hashtable, key, value): # [key, value]
    hash_index = hash_string(key,len(hashtable))
    if key not in hashtable[hash_index]: # which is get_bucket
        hashtable[hash_index].append([key,value])
    return hashtable
    
def hashtable_lookup(hashtable, keyword): # outputs the value associated with that key. If the key is not in the table, output None
    bucket = hashtable_get_bucket(hashtable,keyword)
    for e in bucket:
        if e[0] == keyword:
            return e[1]
    return None
    
def hashtable_update(hashtable, keyword, value): # that updates the value associated with key. If key is already in the table, change the value to the new
# value. Otherwise add a new entry for the key and value.
    if hashtable_lookup == None:
        hashtable_add(hashtable,keyword,value)
    else:
        bucket = hashtable_get_bucket(hashtable,keyword)
        for e in bucket:
            if e[0] == keyword:
                e[1] = value
    return hashtable

    
    
