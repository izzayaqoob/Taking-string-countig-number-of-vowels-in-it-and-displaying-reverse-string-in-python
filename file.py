value=input("Enter any string: ")
count=0
for i in value:
	if i=='a'or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u'or i=='U':
		count=count+1

print('Number of vowels in string: ',count)
lst=[]

index=len(value)
print("Reverse String: ")
while index>0:
	
	print(value[index-1])
	index=index-1
print(lst)

print("Reverse string in one line : ",value[::-1])