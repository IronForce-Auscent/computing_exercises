passes = []
for i in range(4):
    pass_count = 0
    marks = input("Enter marks for test: ")
    m1 = marks[0:2]
    m2 = marks[3:5]
    m3 = marks[6:8]
    m4 = marks[9:11]

    if int(m1) >= 50:
        pass_count += 1
    if int(m2) >= 50:
        pass_count += 1
    if int(m3) >= 50:
        pass_count += 1
    if int(m4) >= 50:
        pass_count += 1
    passes.append(pass_count)

print(passes)
print(passes[0:1:1], passes[3:4:1], passes[7:8:1], passes[9:10:1])
print(passes[7])
print(f"Student 1           {passes[0]} pass(es)")
print(f"Student 2           {passes[1]} pass(es)")
print(f"Student 3           {passes[2]} pass(es)")
print(f"Student 4           {passes[3]} pass(es)")
