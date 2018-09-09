Assignment (Lecture-4)

1. Write a generator function to iterate over first `n` fibonacci numbers.

2. Consider a list of the form:
	```
	[
		(x1, y1, z1),
	 	(x2, y2, z2),
	 	(x3, y3, z3),
	 	.
	 	.
	 	.
	 	(xn, yn, zn)
	 ]
	```
	Transform it to following form:
	```
	[
		(x1, x2, x3, ...., xn),
		(y1, y2, y3, ...., yn),
		(z1, z2, z3, ...., zn)
	]
	```

3. Write a program which takes a text file as input and does following operations sequentially over it:
	- Get list of words present in file
	- Convert all words to uppercase (using map)
	- Remove the words from list which contain 'A' (using filter)
	- Generate a string by concatenating all the words in the final list (using reduce)
