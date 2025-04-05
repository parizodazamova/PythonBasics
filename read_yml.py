import yaml
customers_path = "./data/customer.yml"

with open(customers_path, 'r') as file:
    customers = yaml.safe_load(file)

print(customers['customer1']['CompanyName'])

print(customers['customer1']['Region'])
print(customers['customer1']['PostalCode'])
print(customers['customer1']['PhoneNumbers'])
print(customers['customer1']['PhoneNumbers'][0])

print("--------------------------------------------")
config_path = './data/config.yml'
config = read_yamls_file(config_path) #dictionary


env = 'QA' #[DEV, QA]
for env in ['DEV', 'QA']:
    url = config[env]['url']
    user_name = config[env]['username']
    pword = config[env]['password']

print(f"Open the website : {url}")
print(f"enter username : {username}")
print(f"enter password : {password}")

