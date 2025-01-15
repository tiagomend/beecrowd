def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

def split_input():
    return [int(x) for x in input().split()]

def calculate_duration(start, end):
    return (end - start) if end > start else (1440 - start + end)

def game_time_in_minutes():
    start_hour, start_minute, end_hour, end_minute = split_input()
    start_minutes = hours_to_minutes(start_hour) + start_minute
    end_minutes = hours_to_minutes(end_hour) + end_minute
    
    duration_in_minutes = calculate_duration(start_minutes, end_minutes)
    duration_in_minutes = duration_in_minutes or 1440

    hours, minutes = minutes_to_hours(duration_in_minutes)
    return f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)'


if __name__ == '__main__':
    print(game_time_in_minutes())
