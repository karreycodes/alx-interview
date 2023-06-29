#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i-1]

        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle

def main():
    # Test cases
    test_cases = [0, 1, 5, 10]

    for n in test_cases:
        triangle = pascal_triangle(n)
        print(f"Pascal's Triangle (Level {n}):")
        for row in triangle:
            print(row)
        print()

if __name__ == '__main__':
    main()

