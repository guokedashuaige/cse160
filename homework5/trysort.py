
from operator import itemgetter
student_scores=[('Robert', 8), ('Alice', 9),('Tina', 10),('James', 8)]

sorted_by_name = sorted(student_scores, key=itemgetter(0))
print(sorted_by_name)