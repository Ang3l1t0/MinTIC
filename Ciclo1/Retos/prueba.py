from operator import itemgetter, attrgetter
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('cristian','C',10)
]
print(sorted(student_tuples, key=itemgetter(2,0), reverse=True))