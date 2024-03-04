# ------------------------------------------------------------ # 
# ------------------------- Codewars ------------------------- #
# ---------------- kata - Human Readable Time ---------------- #
# link: https://www.codewars.com/kata/52685f7382004e774f0001f7 #
# ------------------------------------------------------------ #

def make_readable(input_seconds: int) -> str:
    seconds = 0
    minutes = 0
    hours = 0

    for _ in range(input_seconds):
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0

    seconds = seconds if seconds > 9 else '0' + str(seconds)
    minutes = minutes if minutes > 9 else '0' + str(minutes)
    hours = hours if hours > 9 else '0' + str(hours)
    
    return f'{hours}:{minutes}:{seconds}'