def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_spr_prime(n):
    while n != 0 :
        if is_prime(n):
            pass
        else:
            return False
        n = n // 10
    return True

queue = []
temp = []
n = int(input())
for i in range(2,n+1):
    if is_prime(i):
        temp.append(i)
print(temp)
for i in temp:
    if is_spr_prime(i):
        queue.append(i)
print(queue)
for i in range(len(queue)):
    print(queue[i],end = ' ')
print(is_spr_prime(3))
