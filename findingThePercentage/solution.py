if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if student_marks[query_name]:
        count = len(student_marks[query_name])
        totals = sum(student_marks[query_name])
    average = totals / count
    print(f"{average:.2f}")