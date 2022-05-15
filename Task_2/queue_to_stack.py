'''Lab 12.2'''

from arrayqueue import ArrayQueue
from arraystack import ArrayStack

def queue_to_stack(queue):
    '''
    queue to stack
    '''
    return ArrayStack(list(queue)[::-1])

test = ArrayQueue()
