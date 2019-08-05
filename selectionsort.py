# If you're given a list with a bunch of numbers and you're supposed to sort the numbers 
# (with the smallest number on the left and the largest number on the right), 
# how would you do this? There are numerous sorting algorithms to sort numbers in the list. 
# We'll introduce one of the simplest sorting algorithm called selection sort.

testlist_1 = [5, 4, 3, 2, 1]

def selectionsort(some_list):
    count = 0
    for x in range(len(some_list)):
        minimum = some_list[x]
        for j in range(x, len(some_list), 1):
            if some_list[j] < minimum:
                count += 1
                minimum = some_list[j]
                some_list[j], some_list[x] = some_list[x], some_list[j]
        print(x)
    print(count)
    return(some_list)
print(selectionsort(testlist_1))

