items = ["I", "love", "linear", "algebra", "mmmmmmmmmmmmmmmmmmmmmmmm"]
file = open('sample.txt','w')
for item in items:
	file.write(item+"\n")
file.close()