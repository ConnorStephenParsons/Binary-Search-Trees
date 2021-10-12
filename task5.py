class undirected_graph(object):
    """A function which sets the structure for the graph"""
    def __init__(self, graphDictionary):
        if(graphDictionary == None):
            graphDictionary = {}                                                                 #Empty dictionary will be used if no dictionary is provided
        self.graphDictionary = graphDictionary    

    def graph_vertices(self):
        """A function which returns the vertices in the graph, set or created in a list format"""
        return list(self.graphDictionary.keys())
    
    def add_vertices(self, vertices):
        """A function which allows vertices to be added to the graph"""
        if(vertices not in self.graphDictionary):
            self.graphDictionary[vertices] = []                                                  #Vertices with NULL list as a value will be added to the dictionary as a key                                             

    
    def create_edges(self):
        """A function which allows edges to be created or generated"""
        edge = []                                                                                #Edges will be created and put into a list
        for vertices in self.graphDictionary:
            for connection in self.graphDictionary[vertices]:                                    #The edges will form a connection to the vertices in the list
                if({connection, vertices} not in edge):
                    edge.append({vertices, connection})                                          #Edges are able to be added and saved to the disctionary as connections to vertices
        return edge

    def add_edges(self, edges):
        """A function which initialises the edge creation and allows them to be appended to the list from the previous function"""
        edges = set(edges)
        (vert1, vert2) = tuple(edges)                                                            #Vertices can have multiple edges attached to them that is a tuple, list from the 'type set'
        if(vert2 in self.graphDictionary):
            self.graphDictionary[vert2].append(vert1)                                            #If edges are not connected, they are added to the dictionary - connected to specified vertices
        else:
            self.graphDictionary[vert2] = [vert1]
               
  
    def edge(self): 
        """A function which returns the created edge in the graph"""
        return self.create_edges()                                                               
    

    
    
    def isPath(self, startingVertex, endingVertex, graphPath = []):
        """A function which prints out a traversal path between 2 vertices in the graph"""
        g = self.graphDictionary                                                                 #Assign a variable for the graph list
        graphPath = graphPath + [startingVertex]                                                 #Setting a starting vertex from the list for the path traversal
        if startingVertex == endingVertex:                                                       #Returns the graph when the starting vertex reaches the target path
            return graphPath
        if startingVertex not in g:
            return None                                                                          #Returns none if there is no startming vertex in the graph
        for vertices in g[startingVertex]:
            if vertices not in graphPath:
                path = self.isPath(vertices, endingVertex, graphPath)                            #For loop generating a path by assigning all the required arguments to create a new graph from the graph if there is no vertex in the graphPath
                if path == path:
                    return path
        return None        
                
        
    

    
    
    def isConnected(self, visited = None, startingVertex = None):
        """A function which prints out """
        if visited == None:
            visited = set()                                                                       #Sets the visited variable as a tuple type, or list                                                     
        newGraphDictionary = self.graphDictionary                                                 #Defines the graph dictionary inside of a variable for the function            
        graph_vertices = list(newGraphDictionary.keys())                                          #Defines vertices for the newGraphDictionary
        
        if not startingVertex:
            startingVertex = graph_vertices[0]                                                    #Sets the starting vertex as the first index
        visited.add(startingVertex)                                                               #Sets a pointer to the vertex if it has been visited
        if len(visited) != len(graph_vertices):
            for vertices in newGraphDictionary[startingVertex]:                                   #For loop allowing the pointer to be able to 'visit' all vertices in the graph
                if vertices not in visited:
                    if self.isConnected(visited, vertices):
                        return 'yes - the graph is strongly connected'                            #If theres no more vertices to visit, then the graph is connected
        else:
            return 'no - the graph is not strongly connected'
        return 'yes - the graph is strongly connected'                                            #Graph is strongly connected unless there are still vertices to be visited
    
    
    
    def DFSvisited(self, vertices, visited_node):
        """A function which allows the depth first search to see which nodes need to be visited"""
        visited_node[vertices] = False
        print(vertices)                                                                           #Set to False if there are still vertices to be visited
        
        for next_node in self.graphDictionary[vertices]:
            if visited_node[next_node] == True:
                self.DFSvisited(next_node, visited_node)                                          #Once vertices have been visited, the status will be set to True
                
    def depth_first_search(self, vertices):
        """A traversal which starts at rootnode and goes as far along the length of the graph before backtracking to find the traversal"""
        visited_node = [True] * (len(self.graphDictionary))
        
        self.DFSvisited(vertices, visited_node)                                                   #Visited node is set to true when  the visited node is able to be multiplied by all vertices in the vertices in the graph dictionary
        
                
        
        
    def breadth_first_search(self, startingVertex):
        """A traversal which starts at the specified node and prints out a path based on its neighbour nodes"""
        visited_list = []                                                                        #Defined a list for visited nodes
        stack = [startingVertex]                                                                 #Sets the starting vertex for the path in the stack
        while stack:
            vertices = stack.pop()                                                               #Inserts the vertices inside of the stack                                                              
            if vertices not in visited_list:
                visited_list.append(vertices)                                                    #Adds the vertices insode of the stack if they are not already stored there
                queue = self.graphDictionary[vertices]                                           #Puts the vertices inside of the graph dictionary into a queue
                for neighbour in queue:
                    stack.append(neighbour)                                                      #Sets a pointer to the neighbours inside of the queue to determine the path
        return visited_list                                                                      #Returns the path once all of the neighbour nodes have been visited in the stack  
        
    
        
if __name__ == "__main__":
    """Graph creation"""
    graph = {1:[2], 
             2:[3], 
             3:[4,5],     
             4:[3,5], 
             5:[3,4]
            }
    #Assigning the class into a function taking the graph as a paramater for the function calls to use to be able to produce the algorithms for the graph.
    g = undirected_graph(graph)
#######################################################################################
    print("The verices (nodes) in the graph are: ")
    print(g.graph_vertices())

    print("The edges (connections between nodes) in the graph are: ")
    print(g.edge())
########################################################################################
    print("Now adding a vertex (node) of 6: ")
    g.add_vertices(6)
    
    print("The vertices (node) of the new updated grah are: ")
    print(g.graph_vertices())
    
    
    print("Adding the connection for the new node: ")
    g.add_edges({5,6})
    
    print("Updated vertices of graph are: ")
    print(g.graph_vertices())
    
    print("Edges of the updated graph are:" )
    print(g.edge())
############################################################################################    
    print("Now adding a vertex of 7: ")
    g.add_vertices(7)
    
    print("The graph with the new node of 7 added is :")
    print(g.graph_vertices())
    
    print("Adding a connection to the new node:")
    g.add_edges({6,7})
    
    print("Updated version of the graph is: ")
    print(g.graph_vertices())
    
    print("Graph of the updated edges are: ")
    print(g.edge())
############################################################################################    
    
    
    
#Print statement to print the path of the nodes in the graph
            
    print("The path from vertex 1, to vertex 5 is: ")
    file = open('graphPathResult.txt', 'w')
    Path = g.isPath(1, 5)
    print(Path)
    file.write(str(Path))
    file.close()

        
            
                    
###########################################################################################

#Print statement for the isConnected function
print(g.isConnected())
      
      


###########################################################################################

#Print statement for the DFS traversal of the graoph path
file = open ('DFS.txt', 'w')
DFS = g.depth_first_search(int(input('please input a vertex number from the graph to find the depth first search path traversal')))
file.write(str(DFS))
file.close()


###########################################################################################

#Print statement for BFS

file = open ('BFS.txt', 'w')
BFS = g.breadth_first_search(int(input("please input a node from the graph to find the BFS traversal of it"))) 
file.write(str(BFS))
file.close()
print(BFS)











   



  