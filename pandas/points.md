读取csv文件  

test.csv文件内容如下
Tom,20,BeiJing  
Jack,25,Shanghai  


对应test.csv中列名为name，age，addr，但是在文件中没有列名  
读取文件代码如下  

#codingutf-8
import pandas as pd  

header = ['name','age','addr']  

fp = pd.read_csv("test.csv",names=header)  


3、pandas设置索引  
参考：  
http://www.cnblogs.com/hhh5460/p/7067928.html
