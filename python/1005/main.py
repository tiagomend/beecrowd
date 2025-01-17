def average_one():
    a = float(input())
    b = float(input())
    weight_of_a = 3.5
    weight_of_b = 7.5
    media = (a * weight_of_a + b * weight_of_b) / (weight_of_a + weight_of_b)
    return f'MEDIA = {media:.5f}'


if __name__ == '__main__':
    print(average_one())
