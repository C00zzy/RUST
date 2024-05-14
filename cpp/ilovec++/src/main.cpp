#include <iostream>
#include <string>
using namespace std;


int main (){
   string good_langauge = "C++";
   string other_good = "C";
   string user_input;

   cout << "Enter your language:  " << endl;
   cin >> user_input;

   if (user_input == good_langauge){
    cout << "Youre fucking based" << endl;

   } else if (user_input == other_good) {
    cout << "You're pretty good" << endl;
   }

   else {
    cout << "Get outta here" << endl;
   }

   return 0;
}