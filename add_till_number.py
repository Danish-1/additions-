"""this program is written by danish.
 at Fri 25 Dec 2020 , 12:20am. """
 
print("Enter a number to print its additiom from 1 to given number")
#print some information about program.
while True:
# run program again and again
	n = int(input("Enter a number: "))
# take an input from user
#convert it to integer value
	a=0             # assign it 0 to use it as result
	for i in range(1 ,n+1): 
	# 1 to n+1 times
		a +=i       #a =a + i
	print(a)      # print result after end of for loop.
