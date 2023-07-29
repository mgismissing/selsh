CODE = input()
def read(item):
	if CODE[item] == "#": hash(item)
def hash(item):
	act = []
	act.append("FOR")
	act.append(CODE[item + 1])
	if CODE[item + 2] == ":":
		act.append("IN")
		if CODE[item + 3] == "r":
			act.append("RANGE")
			act.append(CODE[item + 4])
		 act.append(CODE[item + 5])
			act.append(CODE[item + 6])
			if CODE[item + 7] == "@":
				act.append("THEN")
				read(item + 8)
			else:
				return "Error", "Syntax"

act = []
read(0)