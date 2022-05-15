import operator
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        su = 0.0000
    query_name = input()
    #for query_name in student_marks.keys():
    su = sum(student_marks.get(query_name))
    avg = su/3
    print("%.2f" % round(avg,2))
