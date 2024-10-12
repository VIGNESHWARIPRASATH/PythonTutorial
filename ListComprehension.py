values = [
    10,
    10,
    "abc",
    20,
    "cdf",
    "cdf",
    100,
    30,
    "ghi"
]
#Normal Method
occurrence = {}
for value in values:
    if not value in occurrence.keys():
        occurrence[value] = 1
    else:
        occurrence[value] += 1
        print("*******Normal Method*******")
        print(occurrence)



#Comprehension Method
occurrence = {value: values.count(values) }
print("******* List Comprehension *******")
print(filterdValues)