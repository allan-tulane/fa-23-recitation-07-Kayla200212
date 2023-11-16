# CMPS 2200 Recitation 10## Answers

**Name:**__kayla willis_______________________
**Name:**__cameron mclaren_______________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work is O(n+m) because it is a breadth first search and the worst case would be if each node and edge is visited once (rather than being able to reach nodes more easily with less edges)
- **4)**
The worst case would depend on the number of connected nodes in the graphs, with the worst case being the number of connected nodes, so n.
- **5)**
This also has a O(n+m) work because it entirely depends on the input from the reachable function's performance. The steps in connected are all at constant time so its work would be that of reachable, which it uses in its computations.
- **7)**
The work would change to O(n^2) because this changes how nodes are stored. It is represented as a matrix, Vertices x Vertices rather than just the addition of the vertex and nodes. 