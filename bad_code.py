# Print the average and the sum of an array of integers
def PRINTsumandAVERAGE(x):
    average = 0

    for i in range(len(x)):
        average += x[i]

    sum = average / len(x)

    print("Sum: " + str(sum))
    print("Average: " + str(average))

    return 0


if __name__ == "__main__":
    # Some testing data
    array = [1, 2, 3]

    PRINTsumandAVERAGE(array)
