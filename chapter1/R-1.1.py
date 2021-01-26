def is_multiple(n, m):
    if m == 0: return False
    return (n % m == 0)

n, m = [int(x) for x in input("Enter two values(n, m) seprated with ',' comma, to cehck weather n in multiple to n \n")]

print(is_multiple(n, m))
