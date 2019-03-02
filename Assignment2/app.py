# This prorgram will compute and calculate the mean and the median of list of data
def main():
    # tell the user what this program is doing
    print("This Program Will Calculate The Mean and The Median Of Data")
    # prompt user how many values that user needs to calculate
    print("How Many Number You Need")
    # let the user know what the number of data that program calculate
    print("Number Should Be Odd like 1 or 3 or 5 or 7")

    number_of_times = int(input())
    # Decaring the acumalate value to hold the sum up of the mean
    mean_holder = 0

    # promt the user that list of data
    input_number = list(eval(
        input("Enter The List Of Data Spilted By Comma , :  ")))

    for n in range(number_of_times):
        # Calculate the mean
        mean_holder += +input_number[n]
    # Report The result of the mean
    print("Mean:")
    mean = round(mean_holder/number_of_times, 2)
    print(f'The Means Of {input_number} is : {mean}')

    # Sorted the list of data as ascending
    num = sorted(input_number)
    # Calculte the result of the median
    median = num[len(input_number)//2]
    # report the median
    print("Median:")
    print(f'The Median of {num} is : {median}')


# invoking the method
main()
