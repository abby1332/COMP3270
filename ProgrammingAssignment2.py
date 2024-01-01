import networkx as nx

fileName = input("Enter text file name: ")

# Create 2D array of connected nodes
with open(fileName, "r") as file:
    data = [[str(x) for x in line.replace('\n', '').split(",")] for line in file]

#Create list of unique nodes and sort them
nodeList = list(set(i for j in data for i in j))
nodeList.sort(key=lambda x: int(x[x.find('_') + 1:]))

# Create 2D array of connected nodes
nodes = {}
for line in open(fileName, 'r'):
    a,b = line.rstrip().split(',')
    if not a in nodes:
        nodes[a] = [b]
    else:
        nodes[a].append( b )

#nodes = dict(nodes.items().sort(key=lambda x: int(x[x.find('_') + 1:], )))
sortedNodes = (sorted(nodes.items(), key=lambda t: t[1]))

print("New method:", sortedNodes)
print(list(nodes.keys()))


fh = open(fileName, "rb")
G = nx.read_edgelist(fh)
fh.close()
print("Data:", data)
print("Node List", nodeList)
print("Graph", G)
file.close()