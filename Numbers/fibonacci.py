#!/usr/local/bin/python3

n = int(input("How long is the Fibonacci sequence you want? "))
seq = [1, 1]

if n < 2:
    print(seq)
else:
    while len(seq) < n:
        seq.append(seq[-1]+seq[-2])

print(seq)
