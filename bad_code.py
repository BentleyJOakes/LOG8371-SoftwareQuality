# Print the average and the sum of an array of integers
def print_sum_and_average(x):
    if not len(array):
        print("The array is empty")
        return

    if not all(isinstance(element, (int, float)) for element in array):
        print("Some elements of the array are not numbers")
        return

    total = 0
    for element in array:
        total += element

    average = total / len(x)

    print("Sum: " + str(total))
    print("Average: " + str(average))


if __name__ == "__main__":
    ## Valid test cases
    array1 = [1, 2, 3] # Sum 6, average 2.0
    array2 = [1.0, 2, 3] # Sum 6.0, average 2.0
    array3 = [1.0, 2.5, 3.45] # Sum 6.95, average 2.3166...

    ## Invalid test cases
    # Should print : Some elements of the array are not numbers
    array4 = ['hello', 2, 3]

    # Should print : The array is empty
    array5 = []

    ## Testing multiple cases
    test_cases = [array1, array2, array3, array4, array5]
    for array in test_cases:
        print_sum_and_average(array)
