eq = '4x**2 +4x +    (-8) =  0'
a = int(eq.replace(' ','').split('x**2')[0])
b = int(eq.replace(' ','').split('x**2')[1].split('x')[0])
c = int(eq.replace(' ', '').replace('(','').replace(')', '').replace('+','').split('x')[-1].split('=')[0])

print(a, b, c) # 4 4 -8

x1 = int((-b+(b**2-4*a*c)**0.5)/(2*a))
x2 = int((-b-(b**2-4*a*c)**0.5)/(2*a))


print(x1, x2) # 1 -2