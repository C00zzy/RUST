#include <stdio.h>
int main(void){ // No arguemnts needed
    int i;
    for(int i = 0; i <= 100; i++) // i is 0 if i is less than 100 it will add to i
    {
        if (i % 3 == 0 && i % 5 == 0)
            printf("FizzBuzz\n");
        else if (i % 3 == 0){
            printf("Buzz\n");
        }
        else if (i % 5 == 0){
            printf("Fizz\n");
        } 
        else{
            printf("%d\n", i);
        }
    }
}