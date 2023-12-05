def calculate_average(lst):
    if not lst:
        return None
    total = sum(lst)
    count = len(lst)
    average = total / count  # GPTLint: Consider directly returning the expression without assigning it to 'average'.
    return average

def string_manipulation(s):
    result = ""
    for char in s:
        result += char + ","  # GPTLint: This can be more efficiently written using str.join().
    return result

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        processed_data = [x * 2 for x in self.data if x > 0]  # GPTLint: Good use of list comprehension.
        return processed_data

def test_func():
    pass  # GPTLint: Function 'test_func' seems to be unused or redundant.

global_variable = 42  # GPTLint: Use of global variables should be minimized.

def use_global_var():
    return global_variable + 10  # GPTLint: Consider passing 'global_variable' as a parameter.

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Average: {calculate_average(numbers)}")
    print(string_manipulation("Hello"))
    processor = DataProcessor(numbers)
    print(processor.process_data())
    print(use_global_var())
