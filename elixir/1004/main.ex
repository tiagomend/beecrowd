defmodule SimpleProduct do
    def calculate_product do
        a = IO.gets("") |> String.trim() |> String.to_integer()
        b = IO.gets("") |> String.trim() |> String.to_integer()
        IO.puts("PROD = #{a * b}")
    end
end

SimpleProduct.calculate_product()
