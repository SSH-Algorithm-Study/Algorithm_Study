length, num  = tuple(map(int,input().split()))
string = input()
count = set()

def dfs(num, old_str, start):
    if num == 0:
        count.add(old_str)
        return
    for i in range(start,length):
        if ord(old_str[i]) < 122:
            new_str = list(old_str)
            new_str[i]= chr(ord(new_str[i]) + 1)
            new_str = "".join(new_str)
        else:
            new_str = old_str
        dfs(num-1,new_str, i)

dfs(length,string,0)
print(len(count)%(10^9+7))