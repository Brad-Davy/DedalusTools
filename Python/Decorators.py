from functools import wraps
import time
from PrintStatements import InitPrint, EndPrint


def timing(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        
        InitPrint()
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time Elapsed: {end-start}")
        EndPrint()

    return wrapped
