# Search methods

import search

ab = search.GPSProblem('A', 'H'
                       , search.romania)

print("Búsqueda en anchura:")
print("----------------------------------------------------------------")
print(search.breadth_first_graph_search(ab).path(), '\n')
print("Búsqueda en profundidad:")
print("----------------------------------------------------------------")
print(search.depth_first_graph_search(ab).path(), '\n')
print("Búsqueda en Ramificación y acotación:")
print("----------------------------------------------------------------")
print(search.bab(ab).path(), '\n')
print("Búsqueda en Ramificación y acotación con subestimación:")
print("----------------------------------------------------------------")
print(search.babsub(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
