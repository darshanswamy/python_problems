# gind longest substring length
#Example input = abcabcbb
# output is 3, answer is abc with length of 3
def find_longest_substring_length(input_str):
    # length is 1 or empty string
    if len(input_str) <= 1:
        return len(input_str)
    count, sub_str = 0, ""

    for s in input_str:
        if s not in sub_str:
            sub_str += s
        else:
            sub_str = sub_str[sub_str.index(s)+1:] + s
        if len(sub_str) > count:
            count = len(sub_str)
    print(sub_str)
    return count


if __name__ == '__main__':
    print(find_longest_substring_length("pwwkew"))