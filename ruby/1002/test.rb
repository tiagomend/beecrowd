require 'minitest/autorun'
require_relative 'main'

class TestCircleArea < Minitest::Test
  def test_first
    input = StringIO.new("2.00")
    $stdin = input
    assert_equal "A=12.5664", calculate_circle_area
  ensure
    $stdin = STDIN
  end

  def test_second
    input = StringIO.new("100.64")
    $stdin = input
    assert_equal "A=31819.3103", calculate_circle_area
  ensure
    $stdin = STDIN
  end

  def test_third
    input = StringIO.new("150.00")
    $stdin = input
    assert_equal "A=70685.7750", calculate_circle_area
  ensure
    $stdin = STDIN
  end
end
