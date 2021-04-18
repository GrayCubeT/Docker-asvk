'''
This module has the calculate function,
which performs all the nesessary actions and returns an answer
'''
from . import myparser as parser
from . import graph
import collections


def bfs(graph, root : graph.Vertex, deleted : graph.Vertex, visited : set): 
    '''
    A slightly altered bfs algorithm that disallows entering one vertex
    Also has a parameter

    Params: a graph, the start of algorithm, the deleted vertex
        and the global visited set

    Returns: a sum of all values
    '''
    if (root in visited):
        # dont count the root if it was visited, moreover
        # this means the supposedly unconnected graphs are connected
        return 0
    queue = collections.deque([root])
    visited.add(root)
    sum = 0
    while (len(queue) > 0):
        vertex = queue.popleft()
        sum += vertex.value
        # if a deleted vertex was in a cylce
        # this bfs will only visit each vertex once
        for neighbour in graph.get(vertex):
            if (neighbour not in visited) and (neighbour is not deleted): 
                visited.add(neighbour)
                queue.append(neighbour)
    return sum

def calculate(data, debug = False, fullans = False):
    '''
    This function parses input from a file and performs the calculations

    Params: a string of data

    Returns: a list of most valuable network stations
    '''
    
    parsed = parser.parser(data)
    if (parsed is None):
        return 'User input error: No input provided'
    if (isinstance(parsed, str)):
        return parsed
    rawedges, vertices = parsed
    # structure parsing 
    graphs = parser.structureGenerator(rawedges)
    
    # print resulting graphs for debug purposes
    if debug:
        print(graphs)
    
    # actual calculation
    
    # ans will hold a list of [vertex, value]
    ans = []
    # run all calculations off every vertex
    for vertex in list(vertices):
        sum = 0
        gr = graphs[vertex.graph]
        # contains a set of all the counted vertices so that nothing gets
        # summed twice
        calculated = set()
        for neighbour in gr.get(vertex):
            sum += bfs(gr, neighbour, vertex, calculated) ** 2
        sum += vertex.value
        ans.append([vertex, gr.value ** 2 - sum])

        # print debug info 
        if (debug):
            print("calculated: " + vertex.name + " change = " + str(gr.value ** 2 - sum))
    
    # sort the answer (this is less complex than bfs of every vertex)
    ans.sort(key = lambda x: x[1], reverse =True)

    # return full answer
    if (fullans):
        return ans
    
    # collect most valuable ones
    ret = [ans[0][0].name]
    i = 1
    while (ans[i][1] == ans[i-1][1]) and (i < len(ans)):
        ret.append(ans[i][0].name)
        i += 1
    return ret

