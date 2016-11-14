import urllib

# standard procedure to read a file
# content = open(path).read()
# open(path).close()

# for website content
# content = urllib.urlopen(url).read()


def read_text():
    sourcefile = open (r"D:\Dropbox\Career\Coding\IntroToPython\movie_quotes.txt") #take address and filename, open it
    # open calls some functions, to create an object from open function
    
    contents_of_file = sourcefile.read() #read the file, which generates text_to_check

    print (contents_of_file)
    sourcefile.close() #close the file
    
    check_profanity(contents_of_file)
    

def check_profanity(text_to_check):
    # get information for a website, use google function
    
    connections = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)

    #urlopen, open a connection to a website, similar to open, need address in string
    # different from webbrowser.open, which just opens a browser
    
    output = connections.read()

    if "true" in output:
        print ("Profanity Alert!!!")
    elif "false"  in output:
        print ("This document has no curse words!")
    else:
        print ("Could not scan the document properly.")

    connections.close()

read_text()
