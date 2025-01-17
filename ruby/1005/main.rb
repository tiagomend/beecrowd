def average_one
  a = gets.to_f
  b = gets.to_f

  weight_of_a = 3.5
  weight_of_b = 7.5

  media = (a * weight_of_a + b * weight_of_b) / (weight_of_a + weight_of_b)

  format("MEDIA = %.5f", media)
end

puts average_one
