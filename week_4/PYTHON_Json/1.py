import json

file_path = 'json1\\data.json'

with open(file_path) as json_file:
    data = json.load(json_file)
    
    

print("Interface status")
print("=" * 80)
print("DN", " " * 38, "Description", " " * 3, "Speed", " " * 8, "MTU")
print("-" * 41, "-" * 13, " ", "-" * 6, " " * 6, "-" * 6)
for imdata in data["imdata"]:
    for i in imdata:    
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t", imdata[i][j]["speed"], "\t", imdata[i][j]["mtu"])

