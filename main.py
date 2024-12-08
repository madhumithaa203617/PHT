def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers) 
    return average

def main():
    numbers = [] 
    print("The average is:", calculate_average(numbers))

if __name__ == "__main__":
    main()
