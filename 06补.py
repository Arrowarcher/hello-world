n=2
s=[1,2,3,4,5,6,7,8,9]
print(s[:n:-1])     #[9, 8, 7, 6, 5, 4]
print(s[n:-1])      #[3, 4, 5, 6, 7, 8]
#也就是说加：会导致反过来做
s2=[1,2,3,4,84,83,82,81,9]
print(s2[:n:-1])
n=5
print(s2[:n:-2])    #从右边取，每次移动2位取
print(s2[:n:1])     #从左边，每次移动1位取
print(s2[:n:2])     #从左边，每次移动1位取
print(s2[n:-2])


#总结：前面加‘:’就变花样了，后面放入数字变成几位取，从右（-）左（+）取
