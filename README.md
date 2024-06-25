# Programming Task 2

## Graph Search Algorithm
### Course: IT00CD89-3005 Graph Algorithms 

-------
**Submitted By:**
**MD Hasibul Haque Zahid (2302302)**

-------

### Application working process
- The program will first ask  whether the graph is directed or not.
- The program will load the graph data from the specified file using the load_graph() 
function. It will parse the file, skipping any headers, and create a data structure representing the graph.
- After loading the graph data, the program will repeatedly ask the user to input the 
start and end nodes for finding paths.
- For each pair of start and end nodes, the program will use Dijkstra's algorithm implemented in the
compute_paths function to find both the shortest and longest paths. It calculates the paths' weights and prints the results.
- After finding paths for a pair of nodes, the program will ask the user if they want to continue
finding paths. If the user chooses to continue, it will prompt for another pair of nodes. If not, the program will exit.
- if a user give an wrong input it will not generate a graph weight , it will ask the user to check the data again.

-------
### This is our input data 
- Vertex1	Vertex2	edge_weight	edge_id
- A	        B	     1	        AB
- B	        C	     2	        BC
- C	        D	     3	        CD
- D	        A	     4	        DA
- A	        C	     5	        AC
- B	        D	     6	        BD

This is a random input choosed by me (Any input will perfectly work in this code)

-------

### Testing Process
- First, we did it in our handbook (Screenshot attached),then we try to implement what we did in out notebook using Dijkstra's algorithm
- Then, we ran the application and given inputs like [Directed,Starting node:A, End Node :C ]
   1. Shortest path from A to C  is ['A', 'B', 'C'] with weight 3 (The value is random we used 1-6 for make it easier to understand)
   2. Longest path from n1 to n6 is ['A', 'C'] with weight 5
- So, for the directed path it gave the correct path measurements what can we verify by looking into the graph (Screenshot Attached)
- After that, we passed inputs for undirected path with values like [Undirected,Starting node: A, End Node: C ]
   1. Shortest path from n1 to n6 is ['A', 'B', 'C'] with weight 7.0 
   2. Longest path from n1 to n6 is ['A', 'D', 'B', 'C'] with weight 12
- We verified that in our handwritten notebook in our hand written note book we also showed another example of test and we succesfully implemeted this in our code

