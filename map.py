mp=[1,2,3,42,23,4]
double=lambda num : num*2
double_mp=map(double, mp)
print(mp)
print(double_mp)
print(list(double_mp))
mp2=map(lambda num: num**2,mp)
print(list(mp2))
custom=filter(lambda x: x<10,mp)
print(list(custom))