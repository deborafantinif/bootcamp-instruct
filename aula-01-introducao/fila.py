# Fila [primeiro elemento a entrar é o primeiro a sair]
# Para seguir esta estrutura no python, é recomendado utilizar uma classe presente 
# no python (colletions.deque) e a partir disso utilizar pops e appends

from collections import deque;

queue = deque([4, 5, 6])

print(queue)

queue.append(9)
queue.append(90)
queue.append(900)

print(queue)

queue.popleft()

print(queue)

queue.popleft()
queue.popleft()

print(queue)
