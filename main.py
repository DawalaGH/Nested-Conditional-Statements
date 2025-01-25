medical_course=input("Did you h`ave a medical course?? Y or N:")
attend=int(input("enter student attendance"))
if medical_course== 'Y':
    if attend>=75:
        print('You are allowed')
    else:
        print("You are not allowed")
else:
    print('You are not allowed') 