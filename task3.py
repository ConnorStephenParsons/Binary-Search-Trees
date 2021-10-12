class undirected_graph(object):
    def __init__(self, graphDictionary):
        if(graphDictionary == None):
            graphDictionary = {}
        self.graphDictionary = graphDictionary    

    def graph_vertices(self):
        return list(self.graphDictionary.keys())

    def edge(self): #this function needs to go under the create edges function when i create it
        return self.create_edges()
    

    def add_vertices(self, vertices):
        if vertices not in self.graphDictionary:
            self.graphDictionary[vertices] = []


    def add_edges(self, edges):
        edges = set(edges)
        (vert1, vert2) = tuple(edges)
        if vert2 in self.graphDictionary:
            self.graphDictionary[vert2].append(vert1)
        else:
            self.graphDictionary[vert2] = [vert1]
            
            

    def create_edges(self):
        edge = []
        for vertices in self.graphDictionary:
            for connection in self.graphDictionary[vertices]:
                if {connection, vertices} not in edge:
                    edge.append({vertices, connection})
        return edge
    
  

#################################################################################
#the next part of this task is to create a function which checks the path between vertices which will be v and w and 
#then print them to a text file.
#
#
#################################################################################

if __name__ == "__main__":
    graph = {1:[2], 2:[3], 3:[4,5], 4:[3,5], 5:[3,4]}

    g = undirected_graph(graph)

    print("the verices (nodes) in the graph are: ")
    print(g.graph_vertices())

    print("the edges (connections between nodes) in the graph are: ")
    print(g.edge())

    print("now adding a vertex (node) of 6: ")
    g.add_vertices(6)

    print("the vertices (node) of the new updated grah are: ")
    print(g.graph_vertices())

    print("adding edges (connections between nodes) to the graph:")
    g.add_edges({4,5})

    print("the vertices (nodes) of the graph with the added edges are: ")
    print(g.graph_vertices())

    print("graph with the updated edges are: ")
    print(g.edge())  

    



    
            
        
    
    
    
    

            