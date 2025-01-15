def simple_product
    a = gets.to_i
    b = gets.to_i
    "PROD = #{a * b}"
end

if __FILE__ == $0
    puts simple_product
end
