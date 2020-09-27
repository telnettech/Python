# Using dunder (__main__) to run from other files like second_app.py
def print_hello():
    print("Hello from app")


if __name__ == '__main__':
    print_hello()
