#include <iostream>

using namespace std;

int main()
{
    char grade;

    cout << "What letter grade:   ";
    cin >> grade;

    switch(grade){
        case 'A':
        cout << "You did great" << endl;
        break;
        case 'B':
        cout << "You failed" << endl;
        break;
        case 'C':
        cout << "You failed" << endl;
        break;
        case 'D':
        cout << "You failed" << endl;
        break;

        default:
        cout << "Not valid" << endl;
    }
}