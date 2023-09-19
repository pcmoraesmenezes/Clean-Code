import threading
import time

# Número de filósofos
NUM_FILOSOFOS = 5

# Semáforos para representar os garfos
garfos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]
"""
garfos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)] significa que
garfos é uma lista de NUM_FILOSOFOS semáforos, cada um com valor inicial 1.

Ou seja, cada filósofo pode pegar um garfo por vez, e o valor 1 significa que
o garfo está disponível para ser pego.

Quando um filósofo pega um garfo, o valor do semáforo correspondente é
decrementado para 0, e quando ele solta o garfo, o valor do semáforo é
incrementado para 1.

Threading.Semafore é uma classe que representa um semáforo, e possui dois
métodos: acquire() e release().

O método acquire() decrementa o valor do semáforo, e o método release()
incrementa o valor do semáforo.

O método acquire() possui um parâmetro opcional chamado blocking, que por
padrão é True. Quando blocking é True, o método acquire() bloqueia a thread
até que o semáforo possa ser decrementado.

O método release() não possui parâmetros, e sempre incrementa o valor do
semáforo.

Threading.Semaphore(1) indica  que o semáforo é binário, ou seja, só pode
assumir os valores 0 e 1. Quando o semáforo é binário, ele é chamado de
mutex, e é usado para controlar o acesso a recursos compartilhados.

Quando o semáforo é binário, o método acquire() é equivalente ao método
lock(), e o método release() é equivalente ao método unlock().

garfos [ threading.Semaphore(1) for _ in range(NUM_FILOSOFOS) ] cria uma lista
de NUM_FILOSOFOS semáforos binários, cada um com valor inicial 1.

É uma list comprehension, que é uma forma compacta de criar uma lista, cria-se
uma lista com NUM_FILOSOFOS elementos, e cada elemento é um semáforo binário
com valor inicial 1.
"""


# Função que simula o pensamento


def pensa(filosofo):
    print(f"Filósofo {filosofo} está pensando")
    time.sleep(1)

# Função que simula a ação de comer


def come(filosofo):
    garfo_esquerdo = filosofo
    garfo_direito = (filosofo + 1) % NUM_FILOSOFOS

    with garfos[garfo_esquerdo]:
        with garfos[garfo_direito]:
            print(f"Filósofo {filosofo} está comendo")
            time.sleep(1)
    print(f"Filósofo {filosofo} terminou de comer e está pensando novamente")


"""
garfo_esquerdo = filosofo, filosofo é um parametro da função come, e indica
qual filósofo está comendo, e cada filósofo tem um garfo a sua esquerda, que
é o garfo com o mesmo número do filósofo.

garfo_direito = (filosofo + 1) % NUM_FILOSOFOS, o garfo a direita do filósofo
é o garfo com o número seguinte ao número do filósofo, e como o número do
filósofo vai de 0 a NUM_FILOSOFOS - 1, o número do garfo a direita é
(filosofo + 1) % NUM_FILOSOFOS.

O operador % é o operador resto da divisão inteira, e é usado para garantir
que o número do garfo a direita seja um número entre 0 e NUM_FILOSOFOS - 1.

with garfos[garfo_esquerdo]:, o with é usado para garantir que o semáforo
correspondente ao garfo a esquerda do filósofo seja liberado quando o filósofo
terminar de comer, mesmo que ocorra uma exceção durante a execução da função
come.

with garfos[garfo_direito]:, o with é usado para garantir que o semáforo
correspondente ao garfo a direita do filósofo seja liberado quando o filósofo
terminar de comer, mesmo que ocorra uma exceção durante a execução da função
come.

"""

# Função que representa a vida de um filósofo


def vida_filosofo(filosofo):
    while True:
        pensa(filosofo)
        come(filosofo)

# Criação de threads para cada filósofo


filosofos = []
for i in range(NUM_FILOSOFOS):
    filosofo = threading.Thread(target=vida_filosofo, args=(i,))
    filosofos.append(filosofo)


"""
filosofo = threading.Thread(target=vida_filosofo, args=(i,)) cria uma thread
que executa a função vida_filosofo, e passa o número do filósofo como
parâmetro.

filosofos.append(filosofo) adiciona a thread criada na lista filosofos.

"""

# Iniciar as threads
for filosofo in filosofos:
    filosofo.start()

# Aguardar todas as threads terminarem
for filosofo in filosofos:
    filosofo.join()
