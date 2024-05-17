#include <iostream>

using namespace std;


int main(){
   int num1, num2;
    char opr;
    cout << "Two numbers";
    cin >> num1 >> num2;
    cout << "Enter operator: ";
    cin >> opr;
    cout << endl;
     switch (opr){
        case '+':
            cout << num1 + num2 << endl;
        break;
        case '*':
            cout << num1 * num2 << endl;
            break;
            default:
            cout << "you cant calculate others yet.." << endl;
    }
    return 0;
 
}