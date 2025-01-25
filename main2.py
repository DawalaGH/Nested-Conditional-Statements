print("select a ride:-")
print("1.bike")
print("2.car")
choice=int(input("Enter your choice:-"))
if choice==1:
 print('Which type of bike?') 
 print('BMX\n')
 print('scooter')
 Choice2=int(input('enter bike type:-'))
 if Choice2==1:
  print('you have selected a BMX')
 else:
  print('you have selected a scooter')
elif(choice==2):
 print("What car do you want")
 print("1.sedan\n")
 print("2.SUV\n")

 choice3=int(input("enter your choice:-"))

 if choice3==1:
  print('You have selected a Sedan')
 else:
  print('You have selected a SUV')
else:
  print('wrong choice')    