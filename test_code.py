import os, sys

class testClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

def some_function():
    x = [1, 2, 3, 4, 5]
    for i in range(len(x)):
        print(x[i])

def some_other_function():
    pass

def main():
    obj = testClass(10, 20)
    print(f"The sum is: {obj.sum()}")
    some_function()
    print("Execution is complete")

if __name__ == "__main__":
    main()
