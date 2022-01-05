def annouce(f):
    def wrapper():
        print("start")
        f()
        print("stop")
    return wrapper 

@annouce 
def hello():
    print("Hi world!")

hello()