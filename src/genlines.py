def generate_lines():
    ver_lines = []
    hor_lines = []
    for i in range(25):
        ver_lines.append([(i * 32, 0),(i * 32, 800)])
        hor_lines.append([(0, i * 32),(800, i * 32)])
    print(ver_lines)
    print(hor_lines)

if __name__ == '__main__':
    generate_lines()