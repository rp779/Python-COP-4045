def find_dup_str(s, n):
    i = 0
    j = i+n
    while i <= (len(s) - 2*n):
        while j <= (len(s) - n):
            # if duplicates :
            if s[i:i+n] == s[j:j+n]:
                # store current substr
                substring = s[i:i+n]
                return substring
                # break
            j += 1
        i += 1
        j = i+n


def find_max_dup(s):
    i = 1
    dup_list = []
    while i <= ((len(s) / 2) - 1):
        n = i
        dup = find_dup_str(s, n)
        if dup != None:
            dup_list.append(dup)
        i += 1
    print(max(dup_list))


s = input("Enter string: \n")
n = int(input("Enter desired length of substring: \n"))
result = find_dup_str(s, n)
print("Result of find_dup_str: {}".format(result))

find_max_dup(s)
