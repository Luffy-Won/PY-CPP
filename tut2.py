
''' cout << "Enter the Hight Value: " << endl;
    double hight;
    cin >> hight;

    cout << "Enter the Width Value: " << endl;
    double width;
    cin >> width;

    double area = hight * width;
    double radius = 2 * (hight + width);

    cout << "Area = " << area << endl;
    cout << "Radius = " << radius << endl; '''


''' hight_value = int(input("enter the Hight Value : "))
width_value = int(input("enter the Width Value : "))

area_value = hight_value * width_value
radius_value = 2 * (hight_value + width_value)

print("The area = " + str(area_value))
print("The radius = " + str(radius_value)) '''

''' password = 0000
user_input = int(input('Enter the pass : '))

if user_input == password:
    print('Your good to go')
else:
    print('Password incorrect')'''

''' choice = int(input('Please chose a Number between 1, 4 : '))

if choice >= 1 and choice <= 4:
   f_numb = int(input('Enter first num : '))
   s_numb = int(input('Enter second num : '))

   if choice == 1:
       print(f_numb + s_numb)
   elif choice == 2:
       print(f_numb - s_numb)
else:
    print('Enter a valid number')'''

''' counter = 0
while counter < 100:
    counter +=1
    print(counter) '''

''' grade = int(input('Enter the mark : '))

sum_mark = 0
counter = 0

while(grade != -1):
    counter +=1
    sum_mark += grade;
    grade = int(input('Enter the mark : '))

print("Total Student No. is = " + str(counter))

print("Mark _sum  Student No. is = " + str(sum_mark))

print("The average is = " + str(sum_mark / counter)) '''

''' for i in range(1, 11):
    print('Harith is awsome') '''

user_input = int(input('Enter your number: '))
while True:
    for i in range(1, 13):
        print(str(user_input) + ' * ' + str(i) + ' = ' + str(user_input * i))

    user_input = int(input('Enter your number: '))
    if user_input == -1:
        break
