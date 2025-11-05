import time

def loading():
    dots = ['Working on it.', 'Working on it..', 'Working on it...']
    for i in dots:
        print(f"{i}\r", end="")
        time.sleep(0.5)
    return
