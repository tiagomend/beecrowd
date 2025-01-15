def calculate_circle_area():
    PI = 3.14159
    raio = float(input())
    return f'A={((raio ** 2) * PI):.4f}'

if __name__ == '__main__':
    print(calculate_circle_area())
