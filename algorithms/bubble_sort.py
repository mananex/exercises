# ---------------------------- #
# --- bubble sort solution --- #
# ---------------------------- #

# sorting up-to-down
def bubble_sort(input_list: list) -> None:
    list_length = len(input_list)
    while True:
        changed = False
        for index in range(list_length):
            if index != list_length - 1 and input_list[index] < input_list[index + 1]:
                changed = True
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
                    
        if not changed: break
