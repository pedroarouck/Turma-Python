from collections import namedtuple, defaultdict, deque


fila_dupla = deque()

fila_dupla.append(1)
fila_dupla.append(2)
fila_dupla.append(3)

print(fila_dupla)

fila_dupla.pop()
print(fila_dupla)
fila_dupla.append(4)
print(fila_dupla)

fila_dupla.popleft()
print(fila_dupla)
fila_dupla.appendleft(5)
print(fila_dupla)