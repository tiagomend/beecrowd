#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double calculate_circle_area()
{
    const double PI = 3.14159;
    double raio;
    cin >> raio;
    return (raio * raio * PI);
}

int main()
{
    cout << fixed << setprecision(4) << "A=" << calculate_circle_area() << endl;
    return 0;
}