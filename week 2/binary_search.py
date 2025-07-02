input_list = list(map(int, input("Enter the sorted elements separated by spaces: ").split()))
search_number = int(input("Enter the number to be found: "))
low = 0
high = len(input_list) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if input_list[mid] == search_number:
        print("The key was found in the list at index:", mid)
        found = True
        break
    elif search_number > input_list[mid]:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("The key is not in the list.")
