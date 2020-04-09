
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

s1.remove('Ahmad')
s2.remove('Sami')
s3.remove('Faris')

x = input('Enter student\'s name')

if x == 'Ahmad':
   count = 0
   for mark in s1:
       count += mark
   print(x , count)
elif x == 'Sami':
    count=0
    for mark in s2:
        count += mark
    print(x , count)
elif x== 'Faris':
    count = 0
    for mark in s3:
        
        count += mark
    print( x , count)
else:
    print("Student is not recorded")
        
    

    
    
