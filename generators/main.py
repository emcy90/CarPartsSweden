from generator_setup import GeneratorSetup


# Creating the Generator Object
generator = GeneratorSetup()

# Load all the lists we need to generate fake data.
my_first_names = generator.load_first_name()
my_last_names = generator.load_last_name()
my_gatuadress = generator.load_gatuadress()
my_house_number = generator.load_house_numbers()
my_zip_codes = generator.load_zip_codes()
my_citys = generator.load_citys()
my_countrys = generator.load_country()
my_company = generator.load_company()
my_phone = generator.load_phone()
my_states = generator.load_states()
reg_no = generator.reg_no_generator()

# Create the strings we need to create a customer.
house_number = generator.create_house_number()
first_name = generator.create_first_name()
last_name = generator.create_last_name()
company = generator.create_company()
phone = generator.create_phone()
street_adress = generator.create_street_adress()
city = generator.create_city()
zip_code = generator.create_zip_code()
country = generator.create_country()
my_sales_representant = generator.create_sales_representant()
state = generator.create_states()

# Create 2 lists so we can combine them to make a customer dict, like
# that one customer generator needs to create a customer.
customer_key_list = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                     'city', 'zip_code', 'country', 'sales_representant', 'states']

customer_list = [first_name, last_name, company, phone, street_adress + " " + house_number, '', city, zip_code,
                 country, my_sales_representant, state]


customer = generator.create_customer_dict(customer_key_list, customer_list)
print(customer)
