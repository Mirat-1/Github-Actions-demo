# app.py

def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def main():
    print(greet("GitHub"))
    print(f"10 + 20 = {add(10, 20)}")


if __name__ == "__main__":
    main()