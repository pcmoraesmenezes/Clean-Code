# Biblioteca Threading do python

### O objetivo é complementar o capítulo 13 do Livro Clean Code, na qual é abordado o tema de concorrência.

## Conceitos Básicos

### O que é concorrência?

Concorrência é a capacidade de um programa de ser executado por mais de um processo ou thread simultaneamente.

### O que é um processo?

Um processo é um programa em execução. Um processo é composto por um ou mais threads.

### O que é um thread?

Um thread é uma sequência de instruções que podem ser executadas simultaneamente com outras sequências de instruções. Um thread é composto por um ou mais processos.

### O que é um programa concorrente?

Um programa concorrente é um programa que possui mais de um thread.

### O que é um programa paralelo?

Um programa paralelo é um programa que possui mais de um processo.

### Semaforo

Um semáforo é um objeto que controla o acesso a um recurso compartilhado por vários processos. Um semáforo é composto por um contador e uma lista de processos que estão esperando para acessar o recurso.

## Biblioteca Threading

```
threading.active_count()
```

Retorna o número de threads em execução.

```
threading.current_thread()
```

Retorna o objeto thread que está sendo executado no momento.

```
threading.get_ident()
```

Retorna o identificador do thread que está sendo executado no momento.

```
threading.enumerate()
```

Retorna uma lista de todos os objetos thread em execução.

```

threading.main_thread()
```

Retorna o objeto thread principal.

```
threading.settrace(func)
```

Define uma função de rastreamento para todos os threads. O parametro a ser passado é uma função que recebe quatro argumentos: frame, event, arg e thread.

```
threading.setprofile(func)
```

Define uma função de perfil para todos os threads. O parametro a ser passado é uma função que recebe três argumentos: frame, event e arg.

```

threading.stack_size([size])
```

Define o tamanho da pilha de novos threads. O tamanho padrão é 0 (sem limite).

```
threading.TIMEOUT_MAX
```

O maior valor de timeout que pode ser usado com métodos de bloqueio.

```

threading.active_count()
```

Retorna o número de threads em execução.

```

threading.excepthook(args)
```

Função padrão chamada quando ocorre uma exceção em um thread que não foi tratada.

### Classe Thread

```
threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

Cria um novo objeto thread. Os parametros são:

- group: deve ser None, é reservado para uso futuro.
- target: função a ser chamada quando o thread iniciar.
- name: nome do thread.
- args: tupla de argumentos posicionais para a função target.
- kwargs: dicionário de argumentos nomeados para a função target.
- daemon: indica se o thread é um daemon.

```
threading.Thread.getName()
```

Retorna o nome do thread.

```
threading.Thread.setName(name)
```

Define o nome do thread.

```
threading.Thread.ident
```

Retorna o identificador do thread.

### Como utilizar a classe thread

```
import threading

def worker():
    print('Worker')

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```
Explicação:
- A função worker() é a função que será executada pelo thread.
- A variável threads é uma lista que irá armazenar os objetos thread.
- O loop for irá criar 5 threads e armazenar na lista threads.
- O método start() irá iniciar o thread.
- target=worker indica que a função worker() será executada pelo thread.

### Classe Lock

```
threading.Lock()
```

Cria um objeto lock. Um lock é um objeto que possui dois estados: locked e unlocked. Um lock é criado no estado unlocked. Um lock possui dois métodos: acquire() e release(). O método acquire() coloca o lock no estado locked e o método release() coloca o lock no estado unlocked.

```
threading.Lock.acquire(blocking=True, timeout=-1)
```

Coloca o lock no estado locked. Os parametros são:

- blocking: indica se o thread será bloqueado até que o lock esteja no estado unlocked.

- timeout: indica o tempo máximo que o thread será bloqueado.

```

threading.Lock.release()
```

Coloca o lock no estado unlocked.

### Como utilizar a classe Lock

```
import threading

lock = threading.Lock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explicação:
- A variável lock é um objeto lock.
- O método acquire() coloca o lock no estado locked.
- O método release() coloca o lock no estado unlocked.

### Objeto Timer

```
threading.Timer(interval, function, args=None, kwargs=None)
```

Cria um objeto timer. Os parametros são:

- interval: intervalo de tempo em segundos.
- function: função a ser chamada quando o timer expirar.
- args: tupla de argumentos posicionais para a função function.
- kwargs: dicionário de argumentos nomeados para a função function.

Exemplo:

```
import threading

def worker():
    print('Worker')

t = threading.Timer(5.0, worker)
t.start()
```

Explicação:
- O objeto t é um timer que irá executar a função worker() após 5 segundos.

```
threading.Timer.cancel()
```

Cancela o timer.

```
threading.Timer.finished
```

Retorna True se o timer já expirou.

```
threading.Timer.is_alive()
```

Retorna True se o timer está em execução.

### Objeto Barrier

```
threading.Barrier(parties, action=None, timeout=None)
```

Cria um objeto barrier. Os parametros são:

- parties: número de threads que devem chamar o método wait() para liberar a barreira.
- action: função a ser chamada quando a barreira for liberada.
- timeout: tempo máximo que uma thread deve esperar para liberar a barreira.

```
threading.Barrier.broken
```

Retorna True se a barreira foi quebrada.

```
threading.Barrier.n_waiting
```

Retorna o número de threads que estão esperando para liberar a barreira.

```
threading.Barrier.parties
```

Retorna o número de threads que devem chamar o método wait() para liberar a barreira.

```
threading.Barrier.wait(timeout=None)
```

Coloca a thread no estado waiting até que o número de threads especificado no parametro parties chame o método wait().

```
threading.Barrier.reset()
```

Reseta a barreira.

### With Statement

```

with threading.Lock():
    # código que será executado com o lock
```

O with statement é utilizado para garantir que o lock será liberado após a execução do código.

### Exemplo de código

```
import threading

lock = threading.Lock()

def worker():
    with lock:
        print('Worker')

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explicação:

- O with statement garante que o lock será liberado após a execução do código.
- É um context manager para o lock.
- O with statement é equivalente a:

```
lock.acquire()
try:
    # código que será executado com o lock
finally:
    lock.release()
```

### Semaphore

```
threading.Semaphore(value=1)
```

Cria um objeto semaphore. Os parametros são:

- value: valor inicial do contador do semaphore.

```
threading.Semaphore.acquire(blocking=True, timeout=None)
```

Decrementa o contador do semaphore. Os parametros são:

- blocking: indica se o thread será bloqueado até que o semaphore esteja no estado unlocked.

- timeout: indica o tempo máximo que o thread será bloqueado.

```
threading.Semaphore.release()
```

Incrementa o contador do semaphore.

```

threading.Semaphore._value
```

Retorna o valor do contador do semaphore.

### Exemplo de código

```
import threading

semaphore = threading.Semaphore(2)

def worker():
    semaphore.acquire()
    print('Worker')
    semaphore.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explicação:

- O semaphore é criado com o valor 2.
- O método acquire() decrementa o contador do semaphore.
- O método release() incrementa o contador do semaphore.

O semaphore ser criado com valor 2 indica que apenas 2 threads podem executar o código ao mesmo tempo.