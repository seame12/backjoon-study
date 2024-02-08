n=[]
for i in range(9):
    n.append(int(input()))
n_max=max(n)
n_index=n.index(n_max)
print(n_max)
print(n_index+1)