require 'minitest/autorun'
require_relative 'main'

class TestSimpleProduct < Minitest::Test
    def test_first
        input = StringIO.new("3\n9\n")
        $stdin = input
        assert_equal "PROD = 27", simple_product
    ensure
        $stdin = STDIN
    end

    def test_second
        input = StringIO.new("-30\n10\n")
        $stdin = input
        assert_equal "PROD = -300", simple_product
    ensure
        $stdin = STDIN
    end
    
    def test_third
        input = StringIO.new("0\n9\n")
        $stdin = input
        assert_equal "PROD = 0", simple_product
    ensure
        $stdin = STDIN
    end
end
