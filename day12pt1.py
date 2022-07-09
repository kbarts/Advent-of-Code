def search(node, path):
    if node == 'end':
        print(path)
        return 1
    else:
        count = 0
        for way in graph[node]:
            if not way.islower() or way not in path:
                new_path = path[:]
                new_path.append(way)      
                count += search(way, new_path)
        return count



lines = open('input12.txt','r').readlines()
graph = {}
count = 0
for num, line in enumerate(lines):
    nodes = line.strip().split('-')
    if nodes[0] in graph:
        graph[nodes[0]].append(nodes[1])
    else:
        graph[nodes[0]] = [nodes[1]]
    if nodes[1] in graph:
        graph[nodes[1]].append(nodes[0])
    else:
        graph[nodes[1]] = [nodes[0]]


print(graph)

print(search('start', ['start']))