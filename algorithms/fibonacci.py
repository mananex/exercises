# ---------------------------- #
# ---- fibonacci solution ---- #
# ---------------------------- #

def fib(n: int) -> int:
    last_number = 0
    current_number = 1
    for _ in range(n - 1): last_number, current_number = current_number, current_number + last_number
    return current_number