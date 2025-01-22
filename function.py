def num(n):
    result=n*2
    print(result)
num(8)
def sum(num1,num2):
    
    result=num1+num2
    return result

total=sum(22,33)
print('total number:',total)
final=num(total)
print(final) #total
# args
def all_sum(num1,num2,*args):
    print(args)
total=all_sum(22,33,44,55,66)
print('total number:',total)
