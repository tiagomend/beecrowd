#include <iostream>
#include <iomanip>

using namespace std;

double averageOne()
{
    double a, b;
    double weightOfA = 3.5, weightOfB = 7.5;

    cin >> a >> b;

    double media = (a * weightOfA + b * weightOfB) / (weightOfA + weightOfB);

    return media;
}

int main()
{
    double result = averageOne();

    cout << fixed << setprecision(5);
    cout << "MEDIA = " << result << endl;

    return 0;
}
