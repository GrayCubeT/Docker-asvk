'''
This module is used for parsing raw input into a structure
'''

from . import graph

def structureGenerator(rawedges):
    graphs = []
    for i in rawedges:
        if not hasattr(i[0], 'graph'):
            # therefore, this is first time this vertex is encountered
            # put a new vertex in a list, create a new graph for it
            gr = graph.Graph(len(graphs))
            graphs.append(gr)
            i[0].graph = gr._id
        if hasattr(i[1], 'graph'):
            # merge two together, update link in graphs variable
            graphs[i[0].graph].merge(graphs[i[1].graph])
            graphs[i[1].graph] = graphs[i[0].graph]
        i[1].graph = i[0].graph

        # now update the graph
        gr = graphs[i[0].graph]
        gr.add(i)
    return graphs


def parser(data):
    '''
    Params: a file

    Returns: a list of edges as a list of pairs of Vertexes

    Notes: file variable can be anything that has a read() attr
    '''
    edgesraw = []
    values = {}
    vertices = {}
    # parse input
    try:
        x = data.replace('\n', ' ')
        
        # change first '{' and last '}' for eval to work correctly
        try:
            lb = x.find("{")
            rb = x.rfind("}")

            x = x[:lb] + '[' + x[lb + 1:rb] + ']' + x[rb + 1:]
        except Exception:
            return 'User input error: brackets not found, please check reference'


        # straight-up evaluate the contents
        try:
            inp = eval(x)
        except Exception as exc:    
            return 'File contents cannot be evaluated: please check reference'
        # correct input checks
        if (not isinstance(inp, (list, set, tuple)) or len(inp) != 2):
            return 'User input error: input should be a list, set or a tuple of 2 objects'
        if (not isinstance(inp[0], (list, set, tuple))):
            return 'User input error: first object is not a list, set or a tuple'
        if (not isinstance(inp[1], (dict))):
            return 'User input error: second object is not a dictionary'
        if (len(inp[1]) > 0 and not hasattr(list(inp[1].values())[0], '__add__')):
            return 'User input error: vertex values should be addable'
        # vertex names are hashable because they are used in a dict
        
        # create and put vertex pairs in a list
        values = inp[1]
        for i in inp[0]:
            # this makes no extra copies of vertices
            first = vertices.get(i[0], graph.Vertex(i[0], values.get(i[0], 0)))
            second = vertices.get(i[1], graph.Vertex(i[1], values.get(i[1], 0)))
            vertices[i[0]] = first
            vertices[i[1]] = second
            edgesraw.append([first, second])
        # check if there are vertices that are not connected to anything
        for i in inp[1].keys():
            if i not in vertices:
                ver = graph.Vertex(i, values.get(i, 0))
                vertices[i] = ver
                # this edge will be accounted for correctly
                edgesraw.append([ver, ver])

    except Exception as exc:
        return 'Undefined user input error: \n' + str(exc)
    return [edgesraw, set(vertices.values())]