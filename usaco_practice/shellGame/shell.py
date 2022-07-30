fin = open ('shell.in', 'r')
lines =int(fin.readline().strip())
print (lines)

data=[]
for i in range(lines):
    line =list(map(int, fin.readline().strip().split()))
    print(line)
    data.append(line)
print(data)

max_list=[0,0,0]

for i in range(3):
    shell=[0,1,2]
    ball=shell[i]
    for line in data:
      
        a=line[0]
        b=line[1]
        g=line[2]
        
        #swap
        t=shell[a-1]
        shell[a-1]=shell[b-1]
        shell[b-1]=t
        print(shell)
      
        if(shell[g-1]==ball):
            max_list[i]+=1
            
print(max_list)
print("max:",max(max_list))

fout = open ('shell.out', 'w')
fout.write(str(max(max_list)))
fin.close()
fout.close()
