#include <iostream>

using namespace std;

int main() {
    // Sales
    
    double sales = 95000;
        cout << "Sales: $" << sales << endl;
    
        // State tax rate
            
            const double stateTaxRate = .04;
                double stateTax = sales * stateTaxRate;
                    cout << "State tax: $" << stateTax << endl;
            
            // County tax rate

            const double CountyTaxRate = 0.2;
                double countyTax = sales * CountyTaxRate;
                cout << "County State Tax: $" << countyTax << endl;               
    return 0;
}
