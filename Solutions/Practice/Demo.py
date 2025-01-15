from collections import defaultdict

countS = defaultdict(list)

countS["a"]=12
countS[12.3]=13

count = {"a":2,"b":3}

count["c"] = 4

print(countS["a"])
print(countS[12.3])


mystring = "6#params4#test"

print(mystring[1+1:1+1+6])

