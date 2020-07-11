d={}

N=int(input())

Cond=list(input().split())

Word=list(input().split())

for i in range(N):
    for j in range(Cond[i],101,Cond[i]):
        if j  in d:
            d[j] = d[j] + " " + Word[i]
        else:
            d[j] = Word[i]

number_list = [d[i] if i in d else str(i) for i in range(1,101)]           

number_lists = ",".join(number_list)

print(number_lists)
