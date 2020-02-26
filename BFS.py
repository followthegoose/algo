from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

graph1 = {}
graph1['you'] = ['kk']
graph1['kk'] = ['you']

search_queue = deque()
search_queue += graph1['you']

def is_seller(name):
    if name[-1] == 'm':
        return True
    else:
        return False

def bfs(search_queue, graph):
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(person):
                print('Продавец найден! Это ' + person)
                return True
            else:
                search_queue += graph[person]
                print('.')
                searched.append(person)
    return False

bfs(search_queue, graph1)