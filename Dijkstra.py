def dijkstra(graph, start, goal):
  distance_min = {}
  track_predecessor = {}
  nodesinv = graph
  inf = float('inf')
  track_path = []
  for nodo in nodesinv:
    distance_min[nodo] = inf
  distance_min[start] = 0

  while nodesinv:
    min_distance_node = None
    for nodo in nodesinv:
      if min_distance_node is None:
        min_distance_node = nodo
      elif distance_min[nodo] < distance_min[min_distance_node]:
        min_distance_node = nodo

    path_op = graph[min_distance_node].items()

    for nodo_hijo, valor in path_op:
      if valor + distance_min[min_distance_node] < distance_min[nodo_hijo]:
        distance_min[nodo_hijo] = valor + distance_min[min_distance_node]
        track_predecessor[nodo_hijo] = min_distance_node

    nodesinv.pop(min_distance_node)
  nodo_actual = goal
  while nodo_actual != start:
    track_path.insert(0,nodo_actual)
    nodo_actual = track_predecessor[nodo_actual]

  track_path.insert(0,start)

  if distance_min[goal] != inf:
    track_path.reverse()
    print('La distancia mas corta es: ' + str(distance_min[goal]))
    print('El camino mas corto es: '+ str(track_path))

grafo = {'A': {'B': 5, 'C': 9},
            'B': {'A': 5, 'E': 10, 'F': 7},
            'C': {'A': 9, 'D': 3, 'E': 5},
            'D': {'C': 3, 'E': 1, 'G': 4},
            'E': {'D': 1, 'B': 10, 'C': 5, 'H': 2, 'G': 4},
            'F': {'B': 7, 'H': 8},
            'G': {'D': 4, 'E': 4, 'I': 12},
            'H': {'F': 8, 'E': 2, 'I': 6},
            'I': {'H': 6, 'G': 12}
            }
dijkstra(grafo,'A', 'E')