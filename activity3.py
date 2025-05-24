def onsquaretime(num):
    iteration=0
    for i in range (num):
        for j in range(num):
            iteration +=1
            print(f"Iteration {iteration}: j={j} i={i}")
    print(f"Total iterations {iteration}")  

onsquaretime(3)
onsquaretime(5)
onsquaretime(4)          