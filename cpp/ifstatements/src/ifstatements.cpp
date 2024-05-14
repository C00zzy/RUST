#include <iostream>

using namespace std;


int main () {
    int age;
    cout << "Enter your age" << endl;
    cout << "This is an 18+ site!" << endl;
    cin >> age;

    if ( age >= 100){
        cout << "you are old as hell.." << endl;
    }
    else if ( age < 0) {
        cout << "How the hell are tying." << endl;
    }

    else if ( age >= 18){
        cout << "you are old as enough" << endl;
    }
    else {
        cout << "You are not old enough kiddo..." << endl;
    }

    return 0;
}