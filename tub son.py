a = int(input())
def tubson(a):
    if a==2:
            return "Tub son"
    elif a==1:
        return "Tub son emas"
    for i in range(2,a):
        if a%i!=0:
            continue
        else:
            return "Tub son emas"
    return "Tub son"
print(tubson(a))
