names = input('Enter Names : ').title().split(",")
assignments = input('Enter Assignments Count : ').split(",")
grades  = input('Enter Grades : ').split(",")

for name, assignment, grade in zip(names, assignments, grades):
	message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
	submit before you can graduate. You're current grade is {} and can increase \
	to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, int(grade) + (2 * int(assignment)))

	print(message)