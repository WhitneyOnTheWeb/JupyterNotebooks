import collections 

class Cache(object):
    
    # Create initial properties of the cache, with nodes as a hash table
    def __init__(self, size):
        self.size = size
        self.nodes = collections.OrderedDict()

    def get(self, node):
        if node in self.nodes:  # If node exists in cache
            value = self.nodes.pop(node)
            self.nodes[node] = value  
            return 'GOT ' + value + '\n'
        else:
            return 'NOTFOUND\n'

    def set(self, node, value):
        if node in self.nodes:
            self.nodes.pop(node)  #Pop the LRU node without retaining the value
        else:
            if len(self.nodes) >= int(self.size):
                self.nodes.popitem(last=False) #Pops the last entry
        self.nodes[node] = value
        return 'SET OK\n'