t = int(input())

string_lengths = []
strings = []

for i in range(t):
    string_lengths.append(int(input()))
    strings.append(input())


for i in range(t):
    if string_lengths[i] < 2:
        print("NO")
        continue
    str_to_list = list(strings[i])

    while len(str_to_list) > 0:
        for k in range(len(str_to_list) - 1):
            if str_to_list[k] == str_to_list[k + 1]:
                str_to_list.pop(k)
                str_to_list.pop(k)
                break
        else:
            print("NO")
            break
    else:
        print("YES")


# what I'm thinking:
# you NEED to start off with at least two characters that are the same adjacent to each other
# effectively, youc an remove these characters from the array and then try again
# if you are able to repeat and get an empty array, then the string is special.

