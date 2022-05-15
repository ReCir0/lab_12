'''Lab 12.2'''

from arraystack import ArrayStack
from arrayqueue import ArrayQueue


def stack_to_queue(stack):
    '''
    stack to queue
    '''
    return ArrayQueue(list(stack)[::-1])

test = ArrayStack()
