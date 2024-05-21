#include <iostream>




int main(){
   int num1, num2;
    char opr;
    std::cout << "Two numbers";
    std::cin >> num1 >> num2;
    std::cout << "Enter operator: ";
    std::cin >> opr;
    std::cout << std::endl;
     switch (opr){
        case '+':
            std::cout << num1 + num2 << std::endl;
        break;
        case '*':
            std::cout << num1 * num2 << std::endl;
            break;
            default:
            std::cout << "you cant calculate others yet.." << std::endl;
    }
    return 0;
 
}