from tanda2poo.ex5.queue import Queue
from tanda2poo.ex5.stack import Stack

#   Crear una pila y apilar algunos elementos.
pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
print('Pila', pila)
print('Tamaño de la pila: ', pila.size)
print('¿La pila está vacía?', pila.is_empty)

#   Desapilar elementos de la pila.
print('Desapilando: ', pila.pop())
print('Desapilando: ', pila.pop())
print('Pila después de desapilar: ', pila)

#   Crear una cola y encolar algunos elementos.
cola = Queue()
cola.enqueue('a')
cola.enqueue('b')
cola.enqueue('c')
print('\nCola: ', cola)
print('Tamaño de la cola: ', cola.size)
print('¿La cola está vacía?', cola.is_empty)

#   Desencolar elementos de la cola.
print('Elemento frontal de la cola:', cola.front())
print('Desencolando: ', cola.dequeue())
print('Desencolando: ', cola.dequeue())
print('Cola después de desencolar: ', cola)

#   Leer el elemnto frontal de la cola.
print('Elemento frontal de la cola:', cola.front())
print('Desencolando: ', cola.dequeue())
