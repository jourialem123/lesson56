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

#explaining using first example (num=3):-
#the i loop will happen n times (in this case 3)
#the j loop will happen n times(3) every i loop which means the j loop will happen 3X3=9 times
#each time the j loop happens the iteration adds 1 so in the end (iteration=9)
#i and j will also update each iteration (for example in iteration 2 the i still didn't finish any loops so i=0 and j is in the second loop so j=2)
#the j restarts every time i increases by one (for example in iteration 4  i=1 because it finished one loop while j=0)