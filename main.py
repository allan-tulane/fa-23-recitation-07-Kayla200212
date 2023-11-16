from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:#need this condition bc when frontier is empty, we're done
        ###TODO
         node = frontier.pop()#remove it from frontier, its our new node
         result.add(node)#this node is part of the final solution in order
         for next in graph[node]:
           if next not in result:#i love python. if the next node isnt alr in result
             frontier.add(next)#add it to the frontier
    return result



def connected(graph):
    ### TODO
    numnodes = len(graph)#num of nodes is the length of graph
    initnode = list(graph.keys()[0])#start node is key 0 on graph
    reach = reachable(graph, initnode)#call reachable
    return len(reach) == numnodes#this is a t/f check.
    #return true if the len of reach is the same as num of nodes




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    result = []
    next = set(graph.keys())#this changes all of our nodes into a set to be parsed
    while len(next) > 0:#continue while there are nodes left
      done = next.pop()#remove
      reach = reachable(graph,done)
      next -= reach#both are sets
      result.append(reach)#add on the node reached
    return len(result)#keep going till out of notes and we just want the #
      

