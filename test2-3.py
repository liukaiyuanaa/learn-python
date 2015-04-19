####-*- coding:uutf-8 -*-
#姓名：柳凯元
#1403050110
#通风1班
#求解物理题
+import math
+a=input('please input a number a=')
+b=input('please input a number b=')
+c=input('please input a number c=')
+d=math.sqrt(b**2-4*a*c)
+root1 = (-b + d)/(2*a)
+root2 = (-b - d)/(2*a)
print 'root1=', root1, ',root2=', root2