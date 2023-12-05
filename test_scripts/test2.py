def calculate_average(lst):
    if not lst:
        return None
    total = sum(lst)
    count = len(lst)
    average = total / count
    return average

def string_manipulation(s):
    result = ""
    for char in s:
        result += char + ","
    return result

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        processed_data = [x * 2 for x in self.data if x > 0]
        return processed_data

def test_func():
    pass

global_variable = 42

def use_global_var():
    return global_variable + 10

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Average: {calculate_average(numbers)}")
    print(string_manipulation("Hello"))
    processor = DataProcessor(numbers)
    print(processor.process_data())
    print(use_global_var())