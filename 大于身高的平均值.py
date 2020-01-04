lis = list(map(int,input().split()))#输入身高的值放入列表中
sum = 0 #初始值为0
for i in range(0,len(lis)):
   sum += lis[i]
aver = sum/len(lis)
for i in range(0,len(lis)):
   if(lis[i]>aver):
      print("{:d} ".format(lis[i]),end = "")
