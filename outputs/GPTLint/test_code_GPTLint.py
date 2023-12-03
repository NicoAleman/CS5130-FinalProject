import os, sys  # GPTLint: Multiple imports on one line are against PEP 8

class testClass:  # GPTLint: Class names should follow CamelCase convention, e.g., TestClass
    def __init__(self, a, b):  # GPTLint: Consider using more descriptive variable names than 'a' and 'b'
        self.a = a
        self.b = b

    def sum(self):  # GPTLint: Method name 'sum' might clash with built-in function name
        return self.a + self.b

def some_function():
    x = [1, 2, 3, 4, 5]
    for i in range(len(x)):  # GPTLint: Consider iterating directly over list items
        print(x[i])

def some_other_function():  # GPTLint: Unused function 'some_other_function'
    pass

def main():
    obj = testClass(10, 20)  # GPTLint: 'testClass' should be 'TestClass' following CamelCase convention
    print(f"The sum is: {obj.sum()}")
    some_function()
    print("Execution is complete")

if __name__ == "__main__":
    main()
