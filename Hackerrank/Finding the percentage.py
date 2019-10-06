if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=0
    for i in range(0,3):
        x=x+student_marks[query_name][i]
    fi=x/3
    print("%.2f"%fi)
