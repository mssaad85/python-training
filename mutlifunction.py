def greeting(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet

hello = greeting("hello, ")
goodbye = greeting("goodbye, ")

hello("saad")
goodbye("saad")
