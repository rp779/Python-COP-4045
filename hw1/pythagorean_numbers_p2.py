n = int(input("Enter range: "))
a = 1
b = 1
c = 1
list_of_triples = []
while c <= n:
    while b < c:
        while a < c:
            if (a**2) + (b**2) == c**2:
                list_of_triples.append((a, b, c))
            a += 1

        b += 1
        a = 1

    c += 1
    b = 1

print(list_of_triples)
