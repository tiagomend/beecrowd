def calculate_circle_area
  pi = 3.14159
  raio = gets.chomp.to_f
  total = format('%.4f', raio ** 2 * pi)
  "A=#{total}"
end

if __FILE__ == $0
  puts calculate_circle_area
end