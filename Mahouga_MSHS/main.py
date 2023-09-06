import mahouga

mahouga_solver = mahouga.MahougaSolver()
test_cases = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
mahouga_solver.build_magic_square(test_cases[0], test_cases[1], test_cases[2])
mahouga_solver.calculate_diagonals()
mahouga_solver.calculate_horizontals()
mahouga_solver.calculate_verticals()
res = mahouga_solver.calculate_magic_square()
print(res)