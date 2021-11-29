from generator_setup import GeneratorSetup

# Creating the Generator Object
generator = GeneratorSetup()

# Load all the lists we need to generate fake data.
car_list_split = []
car_manufacturer_list = []
manufacturer = ""
color = ""
year_model = ""
owner_id = ""
payment_date = ""
payments_no = ""
payment_amount = ""
customer_paid_bill_id = ""

my_first_names = generator.load_first_name()
my_last_names = generator.load_last_name()
my_street_adress = generator.load_street_adress()
my_house_number = generator.load_house_numbers()
my_zip_code = generator.load_zip_codes()
my_city = generator.load_citys()
my_country = generator.load_country()
my_company = generator.load_company()
my_phone = generator.load_phone()
my_states = generator.load_states()
reg_no = generator.reg_no_generator()
colors = generator.load_color()
model = generator.load_car_model()
year = generator.load_year_model()
reg = generator.load_reg_no()
car_list_split, car_manufacturer_list = generator.cars_and_their_manufacturers(car_list_split, car_manufacturer_list)
date = generator.load_date()

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

#print(customer)

# print(car_list_split, car_manufacturer_list)


# Creating a car object
reg_no = generator.random_reg_no()
manufacturer = generator.random_manufacturer()
color = generator.random_color()
model = generator.random_car_model()
year_model = generator.random_year_model()
owner_id = ''

customer_car_key_list = ['reg_no', 'manufacturer', 'color', 'model', 'year_model', 'owner_id']
customer_car_list = [reg_no, manufacturer, color, model, year_model, owner_id]
customer_car = generator.create_customer_car_dict(customer_car_key_list, customer_car_list)
#print(customer_car)


# Creating a payment object
payment_amount = generator.random_amount()
payment_date = generator.random_date()
customer_paid_bill_id = ''

payment_key_list = ['payment_date', 'payment_amount', 'customer_paid_bill_id']
payment_list = [payment_date, payment_amount, customer_paid_bill_id]
payment = generator.create_payment_dict(payment_key_list, payment_list)
# print(payment)

# Creating a order object  -----> How to have customer id less than numbers of customers when creating an order id
# order_date = generator
# required_date = generator
# shipping_date = generator
# status = generator
# comments = generator
# customers_id_customers = rnd_number 
rnd_number = generator.random_customer_order_id() 
print(rnd_number)
