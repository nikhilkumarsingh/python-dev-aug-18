Assignment (Lecture-7)

1. Clear concepts of Git using this video: https://youtu.be/SWYqp7iY_Tc

2. Modify the student_api project such that 
	- `/students/?year=3` returns only those students which are in 3rd year. 
	- `/students/?cgpa=8` returns only those student who have 8 cgpa.
	- `/students/?year=3&cgpa=8` returns those students who are in 3rd year and have cgpa 8.

	Hint: Use `request.args` to get URL parameters dictionary.