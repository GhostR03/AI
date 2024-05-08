def selection_sort_asc(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort_desc(arr):
    n = len(arr)

    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


def menu_driven_selection_sort():
    print("SELECTION SORT")

    length = int(input("\nEnter the number of elements : "))
    arr = []
    for i in range(length):
        num = int(input("Enter element : "))
        arr.append(num)

    while True:
        print("\n1. Sort Ascending")
        print("2. Sort Descending")
        print("3. Exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            sorted_arr = selection_sort_asc(arr)
        elif choice == 2:
            sorted_arr = selection_sort_desc(arr)
        elif choice == 3:
            print("Thank You")
            break
        else:
            print("Invalid choice!")
            return

        print("\nSorted list : ")
        print(sorted_arr)


menu_driven_selection_sort()


























# This code implements a menu-driven approach for selection sort, allowing the user to input elements and choose between sorting the elements in ascending or descending order. Here's a brief explanation of how it works:
#
# 1. **Selection Sort Functions (`selection_sort_asc` and `selection_sort_desc`):**
#    - `selection_sort_asc(arr)`: This function performs selection sort in ascending order on the input array `arr`.
#    - `selection_sort_desc(arr)`: This function performs selection sort in descending order on the input array `arr`.
#
# 2. **Menu-Driven Selection Sort (`menu_driven_selection_sort`):**
#    - The function first asks the user to input the number of elements (`length`) they want to sort.
#    - It then prompts the user to enter each element one by one and stores them in the array `arr`.
#    - After inputting the elements, the function enters a loop where it displays a menu of options:
#      - Option 1: Sort the elements in ascending order using `selection_sort_asc`.
#      - Option 2: Sort the elements in descending order using `selection_sort_desc`.
#      - Option 3: Exit the program.
#      - If an invalid choice is entered, the program returns an error message and exits the function.
#    - After sorting, the sorted array is displayed to the user.
#
# Here's an example usage of the program:
#
# ```
# SELECTION SORT
#
# Enter the number of elements : 5
# Enter element : 34
# Enter element : 12
# Enter element : 56
# Enter element : 7
# Enter element : 23
#
# 1. Sort Ascending
# 2. Sort Descending
# 3. Exit
# Enter your choice : 1
#
# Sorted list :
# [7, 12, 23, 34, 56]
#
# 1. Sort Ascending
# 2. Sort Descending
# 3. Exit
# Enter your choice : 2
#
# Sorted list :
# [56, 34, 23, 12, 7]
#
# 1. Sort Ascending
# 2. Sort Descending
# 3. Exit
# Enter your choice : 3
# Thank You
# ```
#
# You can modify the input elements and test different scenarios using this menu-driven selection sort program.