import os

def rename_files():
    #1 get file names from a folder
    file_list=os.listdir(r"D:\Dropbox\Career\Coding\IntroToPython\alphabet\My Message")

    #add r before the string, means raw path
    # file_list2=os.listdir("D:\\Dropbox\\Career\\Coding\\IntroToPython\\alphabet\\My Message")
    # add r before the path, then don't have to use double \\, could just used r as raw.
    # otherwise, python would ignore single \
    
    # print (file_list)
    #generate a list of filename string

    #return current directory
    
    saved_path = os.getcwd()
    print ("Current Working Directory is " + saved_path)
    
    # change directory
    os.chdir(r"D:\Dropbox\Career\Coding\IntroToPython\alphabet\My Message")
    # os.getcwd(), get current working directory
    # 'D:\\Dropbox\\Career\\Coding\\IntroToPython'
    # os.chdir(path), change path
    # os.chdir('D:\\Dropbox\\Career\\Coding\\')
    # 'D:\\Dropbox\\Career\\Coding'
    
    #2 for each file, rename
    for file_name in file_list:
        print ("Old Name - "+file_name)
        print ("New Name - "+file_name.translate(None, "0123456789")) # could be written as string.translate(file_name,None,'deletechars'), here translate table is none

        os.rename(file_name,file_name.translate(None, "0123456789")) #not in the right direcotry
        

    os.chdir(saved_path) #change back to original saved_path again'''

    
rename_files()

# ---- string.maketrans(from, to) ---- #
# Return a translation table suitable for passing to translate(),
# that will map each character in from into the character at the same position in to;
# from and to must have the same length
# TRANSLATE TABLE IS RETURNED, MORE LIKE A DICT, USED FOR TRANSLATE

# ---- string.translate(s, table[, deletechars]) ---- #
# Delete all characters from s that are in deletechars (if present), and then translate the characters using table,
# which must be a 256-character string giving the translation for each character value, indexed by its ordinal.
# If table is None, then only the character deletion step is performed.

