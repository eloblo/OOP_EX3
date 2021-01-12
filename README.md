# Ex3 Directed Weighted Graph

## The project
this project is an implementation of the directed weighted graph structure in python.   
the main focus is to implement the [Ex2](https://github.com/eloblo/OOP_EX2) java project's graph's classes and
algorithms to python and compare the performance difference between the two,
and the already built library of networkx.   
the project is composed of DiGraph and GraphAlgo classes, a custom json
loader for networkx graphs, along with Junit test with prebuilt graphs in json files.

## Node
a nested class in DiGraph class, represents a vertex in the graph structure.                              
holds a unique id, a position as a tuple of x,y,z coordinates, tag, weight, 
a path list and 2 dictionaries of edges for edges existing him and 
back_edges for edges entering him.      
the class holds the following functions:
* add edge: creates an edge with the given weight. this node will be the source.
  if the edge already exist, does nothing. return if the edge was added.
* add back edge: creates an edge with the given weight,
  while this node is the destination, if the edge doesn't exist, does nothing.    
  return if the edge was added.
* remove edge: remove the edge starting in this node to the given node,
 if the edge doesn't exist, does nothing. return if the edge was removed.
* remove back edge: remove the edge ending in this node from the given node,
 if the edge doesn't exist, does nothing. return if the edge was removed.
* get edges: returns a dictionary of all the edges exiting the node, 
  the destination node's id is the key, and the edge's weight is the value.
* get back edges: returns a dictionary of all the edges entering the node, 
  the destination node id is the key, and the edge's weight is the value.
* get node: returns a dictionary containing the node's id and position.
* get edges list: return a list of dictionaries containing the edges' information.  
* get/set path: return the path / set a new path. if the parameter is none,
  path will be set to an empty list.
* append path: add the given node id to the end of this node's the path.
* get/set tag: return the node's tag / sets the node's tag.
* get/set weight: return the node's weight / sets the node's weight.
* get/set pos: returns the node's position / sets the node's position.
* repr: represent the node as a json format string of the get node dictionary.

## DiGraph
DiGraph is an implementation of the directed weighted graph structure.       
the class holds a dictionary of nodes, an edges counter, and a modification
counter.       
the class has the following functions:
* v size: returns the numbers of nodes in the graph.
* e size: returns the numbers of edges in the graph.
* get mc: returns the numbers of changes done to the graph.
* add node: adds a new node to the graph with the given key.
  if the node already exist, does nothing. returns if the node was added.
* remove node: removes the given node. returns if the node was removed.
  if the node didn't exist, does nothing.
* get all v: return a dictionary containing all the graph's nodes.
* add edge: create an edge between the 2 given nodes, weighing the given weight.
  if the edge already exist, does nothing. return if the edge was added.
* remove edge: removes the edge between the given nodes. return if the edge
  was removed. if the edge didn't exist, does nothing.
* all in edges of: returns a dictionary containing all the edges ending
  in the given node.
* all out edges of: returns a dictionary containing all the edges starting
  in the given node.
* get graph: returns a dictionary containing 2 lists
  of all the edges and all the nodes.
* repr: return the string of the get_graph() dictionary in the format of a json file.  

## GraphAlgo
GraphAlgo is a class full of functions to manipulate the data of it's given DiGraph
graph object. the class holds the following functions:
* get graph: return the current graph.
* load from json: loads a graph from a given path to a json file.
  return if the loading was successful.
* save to json: saves the current graph to a json file.
  return if the saving was successful.
* shortest path: calculate the shortest path from the given source node
  to the given destination node, and the distance of the path.
  the result are returned to the user by a float value of the distance, and
  a list of nodes that make up the path.
* connected component: returns a list of the nodes that make up the strongly
  connected component, that the given node is a part of.
* connected components: returns a list containing the lists of all the strongly
  connected components.
* plot graph: utilizes matplotlib to plot the graph on a GUI.
* set positions: calculates and return the range of the graph's nodes positions
  on the x y axis. if the graph's nodes don't have positions,
  the function create random ones according to current nodes' range.
* clear tag: resets all the graph's nodes' tag to 0,
  to create a sterile graph, so the algorithm could work properly.
* clear weight: resets all the graph's nodes' weight to 0,
  to create a sterile graph, so the algorithm could work properly. 
* repr: returns the string of the repr of the current graph.

## Installation
the project can be easily downloaded using the git clone on the latest commit
and compiled by the relevant programs (pycharm). 


