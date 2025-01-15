defmodule GameTime do
  def hours_to_minutes(hours) do
    hours * 60
  end

  def minutes_to_hours(minutes) do
    hours = div(minutes, 60)
    remaining_minutes = rem(minutes, 60)
    {hours, remaining_minutes}
  end

  def split_input do
    IO.gets("")
    |> String.trim()
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end

  def calculate_duration(start, stop) do
    if stop > start do
      stop - start
    else
      1440 - start + stop
    end
  end

  def game_time_in_minutes do
    [start_hour, start_minute, end_hour, end_minute] = split_input()

    start_minutes = hours_to_minutes(start_hour) + start_minute
    end_minutes = hours_to_minutes(end_hour) + end_minute

    duration_in_minutes =
      case calculate_duration(start_minutes, end_minutes) do
        0 -> 1440
        duration -> duration
      end

    {hours, minutes} = minutes_to_hours(duration_in_minutes)

    IO.puts("O JOGO DUROU #{hours} HORA(S) E #{minutes} MINUTO(S)")
  end
end

GameTime.game_time_in_minutes()
