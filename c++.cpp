#include<iostream>
using namespace std;

// comment in c++  for one line
/*
multiple line comment in c++
*/

int main(){

    // cout << "Hello World" << endl;
    // cout << "My name is Harith" << endl <<"and i am 34 years old" << endl;

    /*
    int age = 29;
    string first_name = "Harith";
    const string last_name = "Alshabibi";
    double gpa = 4.5;
    bool success = true;
    char letter_grade = 'A';

    /* const used so you can't change the value of any varible later example
    last_name = "Naji"; */

    // to change the value of any varible just call the name of the varible without the int or string etc..

    //cout << "My name is " + first_name << endl;

    /* double apple = 30;
    double orange = 40;

    int add = apple + orange;
    int minuse = orange - apple;
    int multi = apple * orange;
    double divied = orange / apple;


    cout << add << endl;
    cout << minuse << endl;
    cout << multi << endl;
    cout << divied << endl; */


    // take input from the user
    /* int current_year = 2020;
    int your_birth_day;
    cout << "Enter your birth year ....";
    cin >> your_birth_day;

    int your_age = current_year - your_birth_day;
    cout << "Your Age is = " << your_age << endl; */

    cout << "You'r name Please ; ";
    string name;
    cin >> name;

    cout << "Nice, How old are You? ";
    int age;
    cin >> age;

    cout << "More and More GOD will ";
    double gpa;
    cin >> gpa;

    cout << "Hello " << name << ", ";
    cout << " Your age is " << age;
    cout << " and Your GPA : " << gpa;



    return 0;
}
