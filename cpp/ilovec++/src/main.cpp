#include <iostream>
#include <string>
using namespace std;


int main (){
   string good_langauge = "C++";
   string user_input;

   cout << "Enter your language:  ";
   cin >> user_input;

   if (user_input == good_langauge){
    cout << "Youre fucking based";

   } else {
    cout << "Get outta here" << endl;
   }

   return 0;
}