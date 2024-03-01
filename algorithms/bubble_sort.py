# ---------------------------- #
# --- bubble sort solution --- #
# ---------------------------- #

arr = [1, 2, 4, 3]

def bubble_sort(input_list: list) -> None:
    list_length = len(input_list)
    while True:
        changed = False
        for index in range(list_length):
            if index != list_length - 1:
                if arr[index] < arr[index + 1]:
                    changed = True
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    print(arr)
                    
        if not changed: break