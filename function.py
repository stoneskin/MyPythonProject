#define recursion function addmore
def addMore(n,max):
    if(n==max):
        result= n
    else:
        result=n+addMore(n+1,max)

    print ("n=",str(n)," result=",str(result))
    return result
#end function addMore

r=addMore(1,100)
print(r)
