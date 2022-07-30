result=0;
for x in range(5):
    v=x+1
    result=result+v;


def AddTo(n):
    result=0;
    for x in range(n):
        v=x+1
       # print("v=",str(v))
        result=result+v;
        #print(result);
    return result;

print("Addto(10)=",str(AddTo(10)))