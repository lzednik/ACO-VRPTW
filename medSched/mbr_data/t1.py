import re
s = "1926-1992 18th Ave, Baldwin, WI 54002, USA"
matched=re.findall('\d+-',s)[0][:-1]
replaced = re.sub('\d+-\d+', matched, s)

print(matched)
print(replaced) 

