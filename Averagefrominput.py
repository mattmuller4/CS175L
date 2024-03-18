#Matthew Muller
#CS-175L
#AverageFromInput

def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            if len(numbers) == 0:
                return 0  
            total = sum(numbers)
            average = total / len(numbers)
            return average
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("File contains non-integer values.")
        return None

filename = "numbers.txt"
average = calculate_average(filename)
if average is not None:
    print("Average:", average)
