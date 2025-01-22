num=[3,4,324,45,34]
odds=[]
for n in num:
    if n % 2==1:
        odds.append(n)
print(odds)
odd_num=[n for n in num if n%2==1]
print(odd_num)