def find_path(graph, start, end, path=[]):  # возврат первого попавшегося пути
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

dict = {}
n = int(input())
for i in range(n):
    a,*b = input().replace(':', ' ').split()
    if a in dict:
        dict[a] += b
    else:
        dict[a] = b

sp =[]
for _ in range(int(input())):
    sp.append(input())

l = len(sp)
dict_out = {}
for j in range(1, l):
    for k in range(j):
        end = sp[k] #предок
        start = sp[j] #потомок
        #print('start - потомок', start, 'end - предок', end)
        if (find_path(dict, start, end,  path=[])) is not None:
            print(start)
            if start in dict_out:
                dict[start] += start
            else:
                dict[start] = start

# for key in dict_out:
#      print(key)