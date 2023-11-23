def printupton(n):
    if n > 0:
        printupton(n-1)
        print(n, end=" ")
