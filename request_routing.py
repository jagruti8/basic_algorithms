# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:03:31 2020

@author: JAGRUTI
"""
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with a root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        # same_parts variable to check if path is already added
        same_parts = 0
        
        # if path is given to be added, then start traversing the Trie from the root.
        if len(parts) != 0:
            node = self.root
            
            for part in parts:
                
                # if the path part is not added, add the part
                if part not in node.children:
                    node = node.insert(part)
                    
                # if path part is already added, go to the next node
                else:
                    same_parts += 1
                    node = node.children[part]
                    
            # if path already exists simply return or else add the handler to the leaf node
            if same_parts == len(parts):
                print("Path already exists")
                return
            node.handler = handler 
            
    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        
        # no parts means root ,i.e, '\' is given, hence root handler is returned
        if len(parts) == 0:
            return node.handler
        
        # trie traversal
        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler
            
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, part):
        # Insert the node as before
        newNode = RouteTrieNode()
        # add the part in the node's children dictionary as a key
        self.children[part] = newNode
        return newNode
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        
        if handler == "":
            print("Error! Enter the handler")
            return
        
        if path == "":
            self.router.root.handler = handler
        
        path_parts = self.split_path(path)
        self.router.insert(path_parts, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        if path == '':
            handler = self.router.root.handler
            if handler:
                return handler
            return self.not_found_handler
        parts = self.split_path(path)
        handler = self.router.find(parts)
        if handler:
            return handler
        return self.not_found_handler
        
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        
        parts = path.split('/')
        parts = [part for part in parts if part!='']
        
        return parts
    
# The below cases are mixture of edge cases and normal cases. 

## 1
# create the router and add a route
router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler") 
router.add_handler("/home/about/me/", "about me handler")
router.add_handler("/home/about/me", "about me handler") # Path already exists
router.add_handler("", "root handler 2") 
router.add_handler("/home/about/me", "") # Error! Enter the handler
router.add_handler("/home/travel/tickets/", "travel tickets handler")
router.add_handler("", "") # Error! Enter the handler

# some lookups with the expected output
print(router.lookup("/")) # root handler 2
print(router.lookup("/home")) # not found handler
print(router.lookup("/home/about")) # about handler
print(router.lookup("/home/about/")) # about handler
print(router.lookup("/home/about/me")) # about me handler
print(router.lookup("/home/about/me/")) # about me handler
print(router.lookup("")) # root handler 2
print(router.lookup("/home/travel/")) # not found handler
print(router.lookup("/home/travel/tickets")) # travel tickets handler
print(router.lookup("/home/travel/tickets/")) # travel tickets handler

## 2
# Here the router has no handler added initially, but later on added

# create the router and add a route
router = Router("", "not found handler") 
router.add_handler("/home/about", "about handler")  
router.add_handler("/home/about/me/", "about me handler")
router.add_handler("/home/about/me", "about me handler")  # Path already exists
router.add_handler("", "root handler") 
router.add_handler("/home/about/me", "") # Error! Enter the handler
router.add_handler("/home/travel/tickets/", "travel tickets handler")

# a bit complicated path
path = "/www.google.com/search?q=router&rlz=1C1CHWA_enIN610IN610&oq=router&aqs=chrome..69i57j0l4j69i60l2j69i61.9967j0j7&sourceid=chrome&ie=UTF-8"
handler = "search results for router handler"
router.add_handler(path, handler)

print(router.lookup("/")) # root handler
print(router.lookup("/home")) # not found handler
print(router.lookup("/home/about")) # about handler
print(router.lookup("/home/about/")) # about handler
print(router.lookup("/home/about/me")) # about me handler
print(router.lookup("/home/about/me/")) # about me handler
print(router.lookup("")) # root handler
print(router.lookup("/home/travel/")) # not found handler
print(router.lookup("/home/travel/tickets")) # travel tickets handler
print(router.lookup("/home/travel/tickets/")) # travel tickets handler
print(router.lookup(path)) # search results for router handler

## 3