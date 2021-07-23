"""
Duplicate Files

Write a function that looks for files with duplicate contents.


For example, let's say you have a directory structure like the following:

root/
    a.txt -> "xyz"
    b.txt -> "1234"
    foo/
       c.txt -> "xyz"
       d.txt -> "abc"
       bar/
           e.txt -> "1234"
           f.txt -> "1234"
           link_to_root -> (symlink to root) <- feel free to exclude these

Some of these files have duplicate contents. The function should return something like this:


>>> def find_duplicates('root')

[['a.txt', 'foo/c.txt'], ['b.txt', 'foo/bar/e.txt', 'foo/bar/f.txt']]

"""


"""
# traverse this directory
# how to tell duplicates

# DFS - like structure
# duplicates - dictionary / hash like structure

# sym link to root link --> "root"

# keep track of visited nodes / traverse like DAG

# os
# list dir

# while traversing, to find "children", use some function to list 
(a) text files in the folder
(b) subfolders

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

https://www.tutorialspoint.com/python/os_listdir.htm

^ returns names of objects in folder
"""

"""
# some type of cache/set to keep track of visited FOLDERs
# some type of data structure (dictionary) to keep track of groups of same text file

keys: text -> list [absolute paths]
# can think about compressing text (keys)

# try using DFS to traverse the structure
# node is the current path

# visiting a node <--> reading the textfiles inside the folder and checking/processing dupliates

^ keep track of absolute path

# utilities: listdir, open/read file

# think about later -- what else does a symlink look like ?
## ^ some utility to check if file is symlink
"""

import os
from os import listdir

          
def duplicate_files(path, duplicates):
          # list the objects
    objects = listdir(path)
    print("objects: ", objects)
    # if this list is empty, return
    if len(objects) == 0:
        return # check this later
    
    # process the node / ie look at the TEXT files
    for ob in objects:
        item = os.path.join(path, ob)
        print("item: ", item)
        if os.path.isfile(item):
            with open(item, 'r') as file:
                data = file.read()
                if data in duplicates:
                    duplicates[data].append(item)
                else:
                    duplicates[data] = [item]
        # else if directory
        if os.path.isdir(item):
            if os.path.islink(item):
                continue
            duplicate_files(item, duplicates)

def process_duplicates(path):
    duplicates = {}
    duplicate_files(path, duplicates)
    
    # get rid of anything that only has one item in the list
    
    # want to return list of lists of absolute paths
    vals = []
    #print("vals process: ", vals)
    print("process duplicates dictionary: ", duplicates)
    for k,v in duplicates.items():
        if len(v) >1:
            vals.append(duplicates[k])
    return vals

# vals = process_duplicates(os.getcwd())
# print("vals: ", vals)


import tempfile

dirpath = tempfile.mkdtemp()

with tempfile.NamedTemporaryFile(dir=dirpath) as tf:
    tf.write("abc".encode('utf-8'))

    with tempfile.NamedTemporaryFile(dir=dirpath) as tf2:
        tf2.write("abc".encode('utf-8'))
#tf = tempfile.NamedTemporaryFile(dir=dirpath) 
        vals = process_duplicates(dirpath)
        print("vals: ", vals)

