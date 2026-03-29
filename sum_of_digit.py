#problem : sum of digit

def Solution(self,num):
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num/10
    return sum

#test cases
#1.num=123
#sum=0  rem=123%10=3 sum=0+3=3  num=123/10=12
#       rem=12%10=2  sum=3+2=5  num=12/10=1
#       rem=1%10=1   sum=3+2+1=6
