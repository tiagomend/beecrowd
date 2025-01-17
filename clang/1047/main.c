#include <stdio.h>
#include <stdlib.h>

int hours_to_minutes(int hours)
{
    return hours * 60;
}

void minutes_to_hours(int minutes, int *hours, int *remaining_minutes)
{
    *hours = minutes / 60;
    *remaining_minutes = minutes % 60;
}

void split_input(int *start_hour, int *start_minute, int *end_hour, int *end_minute)
{
    scanf("%d %d %d %d", start_hour, start_minute, end_hour, end_minute);
}

int calculate_duration(int start, int end)
{
    return (end > start) ? (end - start) : (1440 - start + end);
}

char *game_time_in_minutes()
{
    int start_hour, start_minute, end_hour, end_minute;
    split_input(&start_hour, &start_minute, &end_hour, &end_minute);

    int start_minutes = hours_to_minutes(start_hour) + start_minute;
    int end_minutes = hours_to_minutes(end_hour) + end_minute;

    int duration_in_minutes = calculate_duration(start_minutes, end_minutes);
    if (duration_in_minutes == 0)
    {
        duration_in_minutes = 1440;
    }

    int hours, minutes;
    minutes_to_hours(duration_in_minutes, &hours, &minutes);

    char *result = (char *)malloc(50 * sizeof(char));
    sprintf(result, "O JOGO DUROU %d HORA(S) E %d MINUTO(S)", hours, minutes);

    return result;
}

int main()
{
    char *result = game_time_in_minutes();
    printf("%s\n", result);
    free(result);
    return 0;
}