# '''
# DICTIONARY (HASHMAP)
# A dictionary in Python is a collection of key-value pairs. Each key is connected
# to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# '''

print("#### 1. CREATE ###################")
customer1 = {
    "CustomerID": "ALFKI",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Anders",
    "ContactTitle": "Sales Representative",
    "Address": "Obere Str. 57",
    "City": "Berlin",
    "Region": None,
    "PostalCode": 12209,
    "Country": "Germany",
    "Phone": "030-0074321",
    "Fax": "030-0076545",
}
customer2 = {}
customer3 = dict()
print(customer1)

print("#### 2. READ (ACCESS THE VALUES) ###################")
print(f"ID of the customer: {   customer1['CustomerID']   }")
print(f"Name of the customer: {   customer1['CompanyName']   }")
print(f"The customer is located in: {   customer1['Country'].upper()   }")

print("#### 3. UPDATE ###################")
print(f"The customer city before update: {   customer1['City']   }")
customer1['City'] = "Frankfurt"
print(f"The customer city after update: {   customer1['City']   }")
print(customer1)

print("Adding new info - key-value pair ....")
customer1["isActive"] = True
print(customer1)

print("#### 4. DELETE ###################")
del customer1['Fax']
print(customer1)
removed_info = customer1.pop('Phone')  # returns the value removed
print(customer1)
print(f"Removed value from 'Phone' : {removed_info}")

# removed_info2 = customer1.pop()  # TypeError: pop expected at least 1 argument, got 0

# H/W :
# 1. given a phrase, count how many times each letter was used.
# 2. given a phrase, count how many times vowels( a, e, i, o, and u) were used.
# 3. use dictionary, for loop, if condition, setdefault()
