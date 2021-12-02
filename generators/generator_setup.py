import random


class GeneratorSetup:
    def __init__(self):

        # All lists goes here
        big_first_name_list = []
        big_last_name_list = []
        big_gatuadress_list = []
        big_house_number_list = []
        big_zip_code_list = []
        big_city_list = []
        big_country_list = []
        big_states_list = []
        big_company_list = []
        big_phone_list = []
        reg_no_list = []
        cars_list = []
        manufacturers_list = []
        color_list = []
        car_model_list = []
        year_model_list = []
        amount_list = []
        date_list = []
        status_list = []
        productline_list = []
        text_description_list = []
        html_description_list = []
        image_list = []
        product_list = []
        inprice_list = []
        outprice_list = []
        product_description_list = []
        quantity_list = []
        price_list = []

        rnd_x = 0
        owner_id = 0
        customer_paid_bill_id = 0

        random_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        random_numbers2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                      'W', 'X', 'Y', 'Z']
        customer = {}
        customer_car = {}
        payment = {}
        pay = "0.00"

        # All variables goes here
        the_first_name = ""
        the_last_name = ""
        productdesc = ""
        complete_alpha = ""
        complete_numbers = ""
        f = ""
        line_row = ""
        self.line_row = line_row
        self.f = f
        self.complete_alpha = complete_alpha
        self.complete_numbers = complete_numbers

        self.first_name = self.load_first_name()
        self.last_name = self.load_last_name()

        # Here are the self lists this class uses
        self.big_first_name_list = big_first_name_list
        self.big_last_name_list = big_last_name_list
        self.big_gatuadress_list = big_gatuadress_list
        self.big_house_number_list = big_house_number_list
        self.big_zip_code_list = big_zip_code_list

        self.big_city_list = big_city_list
        self.big_country_list = big_country_list
        self.big_states_list = big_states_list
        self.big_company_list = big_company_list

        self.big_phone_list = big_phone_list
        self.reg_no_list = reg_no_list
        self.cars_list = cars_list
        self.manufacturers_list = manufacturers_list

        self.color_list = color_list
        self.car_model_list = car_model_list
        self.amount_list = amount_list
        self.customer = customer

        self.customer_car = customer_car
        self.payment = payment
        self.pay = pay
        self.random_numbers = random_numbers
        self.owner_id = owner_id
        self.customer_paid_bill_id = customer_paid_bill_id

        self.random_numbers2 = random_numbers2
        self.alpha_list = alpha_list
        self.year_model_list = year_model_list
        self.reg_no_list = reg_no_list

        self.status_list = status_list
        self.date_list = date_list
        self.productline_list = productline_list
        self.text_description_list = text_description_list
        self.html_description_list = html_description_list
        self.image_list = image_list
        self.product_list = product_list
        self.product_description_list = product_description_list
        self.inprice_list = inprice_list
        self.outprice_list = outprice_list
        message = "saab.jpg"
        self.image = bytes(message, 'utf-8')
        self.rnd_x = rnd_x

        self.quantity_list = quantity_list
        self.price_list = price_list

        # **************************************************#
        # Here goes all loading functions this class uses. #
        # *************************************************#

    def load_first_name(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/firstname.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_first_name_list = []
        for names in self.line_row:
            names = names.strip()
            self.big_first_name_list.append(names)
        return self.big_first_name_list

    def load_last_name(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/lastname.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_last_name_list = []
        for last_names in self.line_row:
            last_names = last_names.strip()
            self.big_last_name_list.append(last_names)
        return self.big_last_name_list

    def load_street_adress(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/gatuadress.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_gatuadress_list = []
        for gatuadress in self.line_row:
            gatuadress = gatuadress.strip()
            self.big_gatuadress_list.append(gatuadress)
        return self.big_gatuadress_list

    def load_house_numbers(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/house_numbers.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_house_number_list = []
        for house_number in self.line_row:
            house_number = house_number.strip()
            self.big_house_number_list.append(house_number)
        return self.big_house_number_list

    def load_zip_codes(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/zip_codes.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_zip_code_list = []
        for zip_codes in self.line_row:
            zip_codes = zip_codes.strip()
            self.big_zip_code_list.append(zip_codes)
        return self.big_zip_code_list

    def load_citys(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/city.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_city_list = []
        for city in self.line_row:
            city = city.strip()
            self.big_city_list.append(city)
        return self.big_city_list

    def load_country(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/country.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_country_list = []
        for country in self.line_row:
            country = country.strip()
            self.big_country_list.append(country)
        return self.big_country_list

    def load_states(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/states.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_states_list = []
        for state in self.line_row:
            state = state.strip()
            self.big_states_list.append(state)
        return self.big_states_list

    def load_company(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/company.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_company_list = []
        for company in self.line_row:
            company = company.strip()
            self.big_company_list.append(company)
        return self.big_company_list

    def load_phone(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/phone_numbers.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        # Clean the whitespaces
        self.big_phone_list = []
        for phone in self.line_row:
            phone = phone.strip()
            self.big_phone_list.append(phone)
        return self.big_phone_list

    # ********************************************
    # ****** Here goes the create functions ******
    # ********************************************

    def zip_code_creator(self):
        zip_code = ""
        self.random_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        for number in range(0, 100):
            for x in range(0, 5):
                zip_code = zip_code + random.choice(self.random_numbers)
            print(zip_code)
            zip_code = ""

    def create_adress_house_number(self):
        adress_house_number = ""
        self.random_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.random_numbers2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        counter = 0

        for number in range(0, 100):
            for x in range(0, 2):
                adress_house_number = adress_house_number + random.choice(self.random_numbers)
                temp = adress_house_number

                # A house number should not start with 0
                # if it does we take it away
                if x == 0 and temp == '0':
                    adress_house_number = ""
                    temp = ""
                    counter = 1
                    adress_house_number = temp

                # If the first number was 0 , we dont want the house number
                # to be just 0 so we pick a new number from random list 2
                # who does not have any 0 in it.
                if x == 1 and counter == 1:
                    temp = ""
                    counter = 0
                    temp = temp + random.choice(self.random_numbers2)
                    adress_house_number = temp

            print(adress_house_number)
            adress_house_number = ""
            counter = 0

    def create_sales_representant(self):
        first_name = random.choice(self.first_name)
        last_name = random.choice(self.last_name)
        the_sales_representant = f'{first_name} {last_name:} '
        return the_sales_representant

    def create_first_name(self):
        first_name = random.choice(self.first_name)
        return first_name

    def create_last_name(self):
        last_name = random.choice(self.last_name)
        return last_name

    def create_company(self):
        company = random.choice(self.big_company_list)
        return company

    def create_phone(self):
        phone = random.choice(self.big_phone_list)
        return phone

    def create_street_adress(self):
        street_adress = random.choice(self.big_gatuadress_list)
        return street_adress

    def create_city(self):
        city = random.choice(self.big_city_list)
        return city

    def create_zip_code(self):
        zip_code = random.choice(self.big_zip_code_list)
        return zip_code

    def create_country(self):
        country = random.choice(self.big_country_list)
        return country

    def create_states(self):
        states = random.choice(self.big_states_list)
        return states

    def create_house_number(self):
        house_number = random.choice(self.big_house_number_list)
        return house_number

    # Here goes Dicts this class use
    def create_customer_dict(self, customer_key_list, customer_list):
        self.customer = dict(zip(customer_key_list, customer_list))
        return self.customer

    def create_customer_car_dict(self, customer_car_key_list, customer_car_list):
        self.customer_car = dict(zip(customer_car_key_list, customer_car_list))
        return self.customer_car

    def create_payment_dict(self, payment_key_list, payment_list):
        self.payment = dict(zip(payment_key_list, payment_list))
        return self.payment

    def reg_no_generator(self):  # -----> COMPARE WITH length OF car_reg_no_clean_list??
        self.reg_no_list = []
        for i in range(0, 99):

            for x in range(0, 3):
                alpha_plate = random.choice(self.alpha_list)
                numbers = random.choice(self.random_numbers)

                self.complete_alpha = self.complete_alpha + alpha_plate
                self.complete_numbers = self.complete_numbers + numbers
            complete_reg_no = self.complete_alpha + " " + self.complete_numbers

            # Here we create either a print output with 100 reg_no or we can
            # choose to get the information as a list.
            self.reg_no_list.append(complete_reg_no)
            # print(complete_reg_no)

            # Here we clean the variables before next turn
            complete_reg_no = ""
            self.complete_alpha = ""
            self.complete_numbers = ""
        return self.reg_no_list

    # Function to extract booth cars and manufacturers at the same time.
    def cars_and_their_manufacturers(self, car_list_split, car_manufacturer_list):
        self.cars_list = car_list_split
        self.manufacturers_list = car_manufacturer_list
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/manufacturers.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        for items in self.line_row:
            items = items.strip()
            car_item, maunfacturer_item = items.split(',')
            self.cars_list.append(car_item)
            self.manufacturers_list.append(maunfacturer_item)
        return self.cars_list, self.manufacturers_list
        #  car_item, manufacturer_item = items.strip().split(',')

    def random_manufacturer(self):
        manufacturer = random.choice(self.manufacturers_list)
        return manufacturer

    def load_color(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/colors.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.color_list = []

        for color in self.line_row:
            color = color.strip()
            self.color_list.append(color)
        return self.color_list

    def random_color(self):
        color = random.choice(self.color_list)
        return color

    def load_car_model(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/car_model.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.car_model_list = []

        for model in self.line_row:
            model = model.strip()
            self.car_model_list.append(model)
        return self.car_model_list

    def random_car_model(self):
        car_model = random.choice(self.car_model_list)
        return car_model

    def load_year_model(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/year_model.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.year_model_list = []

        for year in self.line_row:
            year = year.strip()
            self.year_model_list.append(year)
        return self.year_model_list

    def random_year_model(self):
        year_model = random.choice(self.year_model_list)
        return year_model

    def load_reg_no(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/reg_no.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.reg_no_list = []

        for reg in self.line_row:
            reg = reg.strip()
            self.reg_no_list.append(reg)
        return self.reg_no_list

    def random_reg_no(self):
        reg_no = random.choice(self.reg_no_list)
        return reg_no

    def load_date(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/date.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.date_list = []

        for date in self.line_row:
            date = date.strip()
            self.date_list.append(date)
        return self.date_list

    def random_date(self):
        date = random.choice(self.date_list)
        return date

    def random_amount(self):
        self.amount_list = []

        for i in range(200):
            x = round(random.uniform(1.00, 30000.00), 2)
            self.amount_list.append(x)
            self.pay = random.choice(self.amount_list)
        return self.pay

    def load_status(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/status.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.status_list = []

        for status in self.line_row:
            status = status.strip()
            self.status_list.append(status)
        return self.status_list

    def random_status(self):
        status = random.choice(self.status_list)
        return status

    def random_customer_order_id(self):
        self.rnd_x = random.randrange(1, 20)
        return self.rnd_x

    def load_productline(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/productline.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.productline_list = []

        for productline in self.line_row:
            productline = productline.strip()
            self.productline_list.append(productline)
        return self.productline_list

    def load_text_description(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/text_description.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.text_description_list = []

        for text in self.line_row:
            text = text.strip()
            self.text_description_list.append(text)
        return self.text_description_list

    def load_html_description(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/html_description.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.html_description_list = []

        for html_description in self.line_row:
            html_description = html_description.strip()
            self.html_description_list.append(html_description)
        return self.html_description_list

    def load_image(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/image.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.image_list = []

        for image in self.line_row:
            image = image.strip()
            self.image_list.append(image)

        return self.image  # _list

    def load_product_name(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/products.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.product_list = []

        for product in self.line_row:
            product = product.strip()
            self.product_list.append(product)
        return self.product_list

    def load_product_description(self):
        self.f = open('C:/skolan/CarPartsSweden/generators/random_generators/data_files/product_description.txt', 'r',
                      encoding="utf-8")
        self.line_row = self.f.readlines()
        self.f.close()

        self.product_description_list = []

        for productdesc in self.line_row:
            productdesc = productdesc.strip()
            self.product_description_list.append(productdesc)
        return self.product_description_list

    def random_productline(self):
        productline = random.choice(self.productline_list)
        return productline

    def random_text_description(self):
        text_description = random.choice(self.text_description_list)
        return text_description

    def random_html_description(self):
        html_description = random.choice(self.html_description_list)
        return html_description

    def random_productline_image(self):
        image = random.choice(self.image_list)
        return image

    def random_product_name(self):
        product = random.choice(self.product_list)
        return product

    def random_product_descriptions(self):
        description = random.choice(self.product_list)
        return description

    def random_inprice(self):
        self.inprice_list = []

        for i in range(200):
            x = round(random.uniform(1.00, 30000.00), 2)
            self.inprice_list.append(x)
            self.pay = random.choice(self.inprice_list)
        return self.pay

    def random_outprice(self):
        self.outprice_list = []

        for i in range(200):
            x = round(random.uniform(1.00, 30000.00), 2)
            self.outprice_list.append(x)
            self.pay = random.choice(self.outprice_list)
        return self.pay

    # added random owner_id because sqlalchemy is a little bitch not wanting to add things without a fucking owner_id
    def random_owner_id(self):
        self.owner_id = random.randrange(12, 20)
        return self.owner_id

    def random_payment_bill_id(self):
        self.customer_paid_bill_id = random.randrange(1, 20)
        return self.customer_paid_bill_id

    def random_orders_order_no(self):  # -----> FOREIGN KEY (NN)
        self.orders_order_no = random.randrange(1, 3)
        return self.orders_order_no

    def random_products_product_id(self):  # -----> FOREIGN KEY (NN)
        # self.products_product_id = random.randrange(1, ?)
        # return self.products_product_id
        pass

    def random_quantity(self):
        self.quantity_list = []

        for i in range(1):
            x = random.randint(1, 100)
            self.quantity_list.append(x)
            self.pay = random.choice(self.quantity_list)
        return self.pay

    def random_price(self):
        self.price_list = []

        for i in range(1):
            x = round(random.uniform(1.00, 30000.00), 2)
            self.price_list.append(x)
            self.pay = random.choice(self.price_list)
        return self.pay

    def random_first_and_last_name(self):
        first_name = self.create_first_name()
        last_name = self.create_last_name()
        contact_person = first_name + "_" + last_name
        return f'{contact_person}'

    @staticmethod
    def generate_random_email(contact_person):  # INTE KLAR
        email_hosts = ['gmail.com', 'hotmail.com', 'outlook.com', 'live.se', 'yahoo.com']
        contact_person_email = contact_person + "@" + random.choice(email_hosts)
        return contact_person_email  # f'{contact_person}@{random.choice(email_hosts)}'

    print()
    # def random_storage_name(self):
    # self.products_product_id = random.randrange(1, ?)
    # return self.products_product_id
    # pass
