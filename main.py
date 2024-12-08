def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total=0
    for num in numbers:
         total+=num
         average = total / len(numbers) 
    return average

def main():
    numbers = []

    n=int(input("Enter the total length of the list:"))
    for i in range(1,n+1):
        count=1
        a=int(input("Enter the element" ))
        print("The",count,"element is",a)

        numbers.append(a)
        count+=1
    print("The average is:",calculate_average(numbers))

if __name__ == "__main__":
    main()
