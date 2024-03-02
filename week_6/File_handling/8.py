import os
if os.path.exists("deleted.txt"):
  os.remove("deleted.txt")
else:
  print("The file does not exist")