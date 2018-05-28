# README
**Author:**   Whitney King / @whitneyontheweb
**Project:**  LRU Cache Task
**Date:**     2/21/2018
**Language:** Python 2.7.13

### Design Requirements

Design and implement an LRU (Least Recently Used) cache. 

- This is a cache with a fixed size in terms of the number of items it holds (supplied at instantiation). 
- For this exercise, we won’t worry about the number of bytes. 
- Your program can treat the keys and values as strings. 
- You don’t need to support keys or values that contain spaces. 
- The cache must allow client code to get items from the cache and set items to the cache. 
- Once the cache is full, when the client wants to store a new item in the cache, an old item must be overwritten or removed to make room. 
- The item we will remove is the Least Recently Used (LRU) item. 
- The cache should consider an item to have been used anytime that item is set or retrieved. 
- Note that your cache does not need persistence across sessions.
- Read input from stdin and print output to stdout 

### Design

I opted to write this in Python 3 and then check compatibility in Python 2, as to work within the specified environment.

### Algorithm / Pseudocode

The algorithm can be written with get/set functions, accompanied by an OrderedDict acting as a numbered hash table. The position of the node in the cache indicates most recent use (first item is LRU).

- Get input
- Check size
- Parse Input
- If node exists in cache
    - Return and replace node
- If node does not exist in cache:
    - If nodes are open:
        - Set node into last position
    - If no nodes are open:
        - `Pop` LRU node from cache 
        - Set node into last position

### Run Instructions

Double click wl_lrucache.py to run the program in a Python 2.7.13 environment, or run it from your preferred IDE


### Known Issues, Limitations, and Assumptions

Limitations are lack of use of many packages that would otherwise make a LRU algorithm not need to be rewritten. In this context, this is how I'd write one if no Python packages existed to help, aside from the collections package.

Additionally, I haven't considered myself a speed coder in the past, so the two hour limitation was initially daunting. For this reason, I decided it was best to sleep on how I would go about putting this together and tackled it this morning from 9:45 - 11:45am.

Unfortunately there is at least one bug in the final output, but I didn't want to go over my allotted time to fix it.