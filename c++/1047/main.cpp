#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int hours_to_minutes(int hours)
{
    return hours * 60;
}

pair<int, int> minutes_to_hours(int minutes)
{
    int hours = minutes / 60;
    int remaining_minutes = minutes % 60;
    return make_pair(hours, remaining_minutes);
}

vector<int> split_input()
{
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> input;
    int num;
    while (ss >> num)
    {
        input.push_back(num);
    }
    return input;
}

int calculate_duration(int start, int end)
{
    return (end > start) ? (end - start) : (1440 - start + end);
}

string game_time_in_minutes()
{
    vector<int> time = split_input();
    int start_hour = time[0], start_minute = time[1];
    int end_hour = time[2], end_minute = time[3];

    int start_minutes = hours_to_minutes(start_hour) + start_minute;
    int end_minutes = hours_to_minutes(end_hour) + end_minute;

    int duration_in_minutes = calculate_duration(start_minutes, end_minutes);
    if (duration_in_minutes == 0)
        duration_in_minutes = 1440;

    pair<int, int> time_duration = minutes_to_hours(duration_in_minutes);
    int hours = time_duration.first;
    int minutes = time_duration.second;

    stringstream result;
    result << "O JOGO DUROU " << hours << " HORA(S) E " << minutes << " MINUTO(S)";
    return result.str();
}

int main()
{
    cout << game_time_in_minutes() << endl;
    return 0;
}
