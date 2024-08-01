#include <stdio.h>
#include <math.h>

// Define the structure to hold variables used in calculations
struct variables {
  int num1;          // First integer input for arithmetic operations
  int num2;          // Second integer input for arithmetic operations
  int sum;           // To store the result of addition, subtraction, multiplication
  long opr;          // To store the operation selected by the user (note: should be char for operations)
  double S;          // Input number for square root calculation
  double tolerance;  // Tolerance for square root approximation
  int range;         // Range for printing even and odd numbers
};

// Function prototypes
void HELPfunc(void);            // Displays help information
void subtraction(struct variables v); // Performs subtraction
void multiplication(struct variables v); // Performs multiplication
void addition(struct variables v); // Performs addition
void dividson(struct variables v); // Performs division
double sqrtroot(struct variables v); // Computes the square root

// Displays help information about available operators
void HELPfunc(void) {
  printf("Operators:\n");
  printf("+ for addition\n");
  printf("- for subtraction\n");
  printf("* for multiplication\n");
  printf("/ for division\n");
  printf("s for square roots\n");
  printf("d To print even and odd numbers\n");
}

// Performs subtraction and prints the result
void subtraction(struct variables v) {
  v.sum = v.num1 - v.num2;
  printf("Difference: %d\n", v.sum);
}

// Performs multiplication and prints the result
void multiplication(struct variables v) {
  v.sum = v.num1 * v.num2;
  printf("Product: %d\n", v.sum);
}

// Performs division and prints the result
void dividson(struct variables v) {
  if (v.num2 == 0) { // Check for division by zero
    printf("CANNOT DIVIDE BY 0!\n");
  } else {
    v.sum = v.num1 / v.num2; // Perform division (fix: should be integer division)
    printf("Quotient: %d\n", v.sum);
  }
}

// Computes the square root using the Newton-Raphson method
double sqrtroot(struct variables v) {
  if (v.S < 0) { // Check for negative input
    printf("ERROR: Negative input for square root!\n");
    return -1; // Return error code
  }
  double num1 = v.S;
  double num1_next;

  // Iteratively improve the estimate of the square root
  do {
    num1_next = 0.5 * (num1 + v.S / num1);
    printf("Current estimate: %.10f, Next estimate: %.10f\n", num1, num1_next);
    if (fabs(num1_next - num1) < v.tolerance) {
      break; // Exit loop if the result is within the tolerance
    }
    num1 = num1_next;
  } while (1);

  return num1_next; // Return the calculated square root
}

// Performs addition and prints the result
void addition(struct variables v) {
  v.sum = v.num1 + v.num2;
  printf("Sum: %d\n", v.sum);
}

int main(void) {
  struct variables v;
  v.tolerance = 1e-6; // Set the tolerance for square root calculation
  char input[10];
  
  while (1) { // Infinite loop to continuously prompt user
    printf("Welcome! press h or H for help!\n");
    scanf(" %c", &v.opr); // Read user input for operation

    // Handle the 'd' operation to print even and odd numbers
    if (v.opr == 'd') {
      printf("What range?\n");
      scanf("%d", &v.range); // Read the range from the user
      for (int i = 0; i < v.range + 1; i++) { // Print numbers from 0 to range
        if (i % 2 == 0) {
          printf("%d: odd\n", i); // 'odd' for even index (but this seems like a logic error)
        } else {
          printf("%d: even\n", i); // 'even' for odd index (but this seems like a logic error)
        }
      }
      continue; // Skip the rest of the loop and prompt the user again
    }

    // Handle the 's' operation for square root calculation
    if (v.opr == 's') {
      printf("What number for square root?\n");
      scanf("%lf", &v.S); // Read the number for square root calculation
      double result = sqrtroot(v);
      if (result >= 0) {
        printf("The square root of %.2f is %.6f\n", v.S, result);
      } else {
        printf("ERROR\n");
      }
      break; // Exit the loop after calculating square root
    }

    // Handle the 'h' operation to display help
    if (v.opr == 'h') {
      HELPfunc();
      continue; // Skip the rest of the loop and prompt the user again
    }

    // Prompt the user for two integers for arithmetic operations
    printf("Enter two integers! \n");
    scanf("%d %d", &v.num1, &v.num2);

    // Perform the selected arithmetic operation
    switch (v.opr) {
      case '+':
        addition(v);
        break;
      case '-':
        subtraction(v);
        break;
      case '/':
        dividson(v);
        break;
      case '*':
        multiplication(v);
        break;
      default:
        printf("Invalid operation!\n");
        break;
    }
  }
  return 0;
}
// comments added by AI.
