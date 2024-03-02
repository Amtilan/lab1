items = ["I", "am", "KBTU", "student", "fortunately"]
file = open('sample.txt','w')
for item in items:
	file.write(item+"\n")
file.close()