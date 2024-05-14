#include <iostream>

using namespace std;

<<<<<<< HEAD
int main()

int month;
cout << "Enter the month (1-12):  ";
cin >> month;


switch(month){
    case 1:
        cout >> "It is january";
        break;
          case 2:
        cout >> "It is feburary";
        break;
          case 3:
        cout >> "It is march";
        break;
          case 4:
        cout >> "It is april";
        break;
          case 5:
        cout >> "It is may";
        break;
}
=======

int main () {
    int month;
    cout << "Enter the month";
    cin >> month;
    
    switch(month){
        case 1:
        cout << "It is january" << endl;
        break;
        case 2:
        cout << "It is feburary" << endl;
        break;
        default:
        cout << "Please enter 1 through 12 bruh";
    }

}
>>>>>>> 11485df (	new file:   cpp/.vscode/settings.json)
