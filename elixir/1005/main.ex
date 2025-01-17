defmodule AverageOne do
  def calculate_media() do
    a = IO.gets("") |> String.trim() |> String.to_float()
    b = IO.gets("") |> String.trim() |> String.to_float()

    weight_of_a = 3.5
    weight_of_b = 7.5

    media = (a * weight_of_a + b * weight_of_b) / (weight_of_a + weight_of_b)

    IO.puts("MEDIA = #{:erlang.float_to_binary(media, decimals: 5)}")
  end
end

AverageOne.calculate_media()
