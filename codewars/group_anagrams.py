# ------------------------------------------------------------ # 
# ------------------------- Codewars ------------------------- #
# ------------------ kata -- Group Anagrams ------------------ #
# link: https://www.codewars.com/kata/537400e773076324ab000262 #
# ------------------------------------------------------------ #

def group_anagram(alphabetical_anagram: str, anagrams: list) -> list:
    result_list = []
    for anagram in anagrams:
        if alphabetical_anagram == ''.join(sorted(anagram)):
            result_list.append(anagram)
    return result_list

def group_anagrams(anagrams: list) -> list:
    disabled_anagrams = []
    result_list = []
    for specified_anagram in anagrams:
        anagram_alphabetical = ''.join(sorted(specified_anagram))
        if anagram_alphabetical not in disabled_anagrams:
            result_list.append(group_anagram(anagram_alphabetical, anagrams))
            disabled_anagrams.append(anagram_alphabetical)
    return result_list