'''




'''

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)
        else:
            print("BIG TIME ERROR")
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # create an empty queue and add starting vertex to it
        queue = []
        queue.append(starting_vertex_id)

        # this will keep track of all next_to_visit_vertices
        #create an empty set to keep track of visited vertices
        visited = set()
        #While queue is not empty
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            #dequeue a vertex off the queue
            #if vertex is not in visited vertices
            if current_vertex not in visited:
                print(current_vertex)
                #print it

                #add the vertex to out visited list
                visited.add(current_vertex)
                #add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

        def dft(self, starting_vertex_id):
        # create an empty queue and add starting vertex to it
        stack = []
        stack.append(starting_vertex_id)

        # this will keep track of all next_to_visit_vertices
        #create an empty set to keep track of visited vertices
        visited = set()
        #While queue is not empty
        while len(queue) > 0:
            current_vertex = stack.pop()
            #dequeue a vertex off the queue
            #if vertex is not in visited vertices
            if current_vertex not in visited:
                print(current_vertex)
                #print it

                #add the vertex to out visited list
                visited.add(current_vertex)
                #add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

        def bfs(self, starting_vertex_id, target_vertex_id):
           #create an emptyquque and add a path to starting vertex
            
            #create a visited set
            #while queue is not empty:
                #dequeue the current PATH from the queue

                #get the current vertex from the path
                #use the vertex at the end of the path array

                #if the vertex is not visited
                    #add vertex to the visited list

                    #CHECK IF CURRENT VERTEX IS THE TARGET VERTEX:
                        #we found our vertex and the path to it
                        #return the PATH

                    #for each neighbor of current vertex
                        #add the path to that neighbor, to the queue
                            #copy the current path
                            #add neighbor to the path
                            #add the whole path to the Queue

our_graph = Graph()

our_graph.add_vertex(1)
our_graph.add_edge(1,2)
our_graph.add_vertex(2)

print(our_graph.vertices)