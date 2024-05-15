n = 0
print("n a b c d")
for a in range(1,22):
    for b in range(1,12):
        for c in range(1,8):
            for d in range(1,7):
                if a + 2 * b + 3 * c + 4 * d == 30:
                    n += 1
                    print(n, a, b, c, d)
