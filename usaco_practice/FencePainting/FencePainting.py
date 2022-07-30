## http://www.usaco.org/index.php?page=viewproblem2&cpid=567
#Problem 1. Fence Painting 
import sys

fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')

a,b =map(int, fin.readline().strip().split())
c,d =map(int, fin.readline().strip().split())

# sys.stdin = open("paint.in", "r");
# sys.stdout = open("paint.out", "w")

# a, b = map(int, input().split())
# c, d = map(int, input().split())

#print(a,b,c,d)

min=min([a,c]);
max=max([b,d]);

ct=0;
print(f"{min} {max}")
for x in range(min,max):
    if (x>=a and x<=b) or (x>=c and x<=d):
        if(x>=b and x<c) or (x>=d and x<a):
            continue;
        print(x)
        ct+=1;
        
print(ct);
fout.write(str(ct));
fin.close()
fout.close()