'''
from urllib import request

csv_url="https://s3.amazonaws.com/back-end-training/house-prices.csv"

def download_csc(csv_url1):
	response = request.urlopen(csv_url1)
	#print(response.read())
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	for line in lines:
		number_array=line.split(",")
		print (number_array)
	print (len(lines))
	# fw = open("data_number.csv","w")
	# for line in lines:
	# 	fw.write(line + "\n")
	# fw.close()

download_csc(csv_url)
'''

#main code 
sum_x=0
sum_y=0
sum_xy =0
sum_xx = 0
sum_yy = 0
n=0

fr = open ("data_number.csv","r")
data_text = fr.readlines();
for data in data_text:
	number = data.split(",")
	sum_x = sum_x + int(number[1])
	sum_y = sum_y + int(number[0])
	sum_xy = sum_xy + int(number[1])*int(number[0])
	sum_xx = sum_xx + int(number[1])**2
	sum_yy = sum_yy +int(number[0])**2
	n= n+1

A = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_xx)-(sum_x**2))
B = ((sum_y*sum_xx)-(sum_x*sum_xy))/((n*sum_xx)-(sum_x**2))

print ("the equation is Y = " +str(A)+" X + " + str(B))

Q = float(input("Enter the Area"))

cal = A * Q + B

print (cal)

