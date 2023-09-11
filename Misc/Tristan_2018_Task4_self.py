students = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
results = []
score_sum = 0

for i in range(6):
    marks = input(f"Enter results for student {i + 1}: ").split(",")
    results.append([marks[_].strip() for _ in range(4)])

for i in range(6):
    for x in range(4):
        score = int(results[i][x])
        if score >= 50:
            students[i + 1] += 1
        score_sum += score

response = f"""
Student 1       {students[1]} pass(es)
Student 2       {students[2]} pass(es)
Student 3       {students[3]} pass(es)
Student 4       {students[4]} pass(es)
Student 5       {students[5]} pass(es)
Student 6       {students[6]} pass(es)
Average marks  {round(score_sum / 24, 1)}
"""
print(response)