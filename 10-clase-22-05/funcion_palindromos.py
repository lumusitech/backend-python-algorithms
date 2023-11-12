def palindromico(n):
    u=str(n%10)
    d=str(n//10%10)
    c=str(n//10//10%10)
    if c+d+u==u+d+c:
        return True
    else:
        return False

print(palindromico(124))
