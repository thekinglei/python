Python中如何判断变量是否已经定义
Python中其实有蛮多方法可以判断一个变量是否已经定义了。

方法一：try except

def  isset(v):  
     try :  
         type (eval(v))  
      except :  
          return   0   
      else :  
          return   1   
用法：

if isset('user_name'):  
    print 'user_name is defined'  
else  
    print 'user_name is not defined'  
方法二：使用命名空间

'varname' in locals().keys()
'varname'  in   dir()Python中如何判断变量是否已经定义