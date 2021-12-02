import random

from generators.generator_setup import GeneratorSetup


class CpsCreator(GeneratorSetup):
    def __init__(self):
        super().__init__()

        # class variables:
        generator = GeneratorSetup()
        storage = ""
        storage_name = ""
        storage_quantity = ""
        storage_city = ""
        storage_key_list = []
        staffs_key_list = []
        staffs = ""
        first_name = ""
        last_name = ""
        job_title = ""
        phone = ""
        reports_to = ""
        store = ""
        cps_orders_key_list = []
        cps_orders = ""
        order_date = ""
        required_date = ""
        shipping_date = ""
        status = ""
        comments = ""
        order_no_comments = ""
        suppliers_key_list = []
        suppliers = ""
        supplier_name = ""
        supplier_adress1 = ""
        supplier_adress2 = ""
        city = ""
        zip_code = ""
        country = ""
        contact_person = ""
        phone_number = ""
        email = ""
        storage_has_products_list = []
        manufacturers_key_list = []
        manufacturers = ""
        name_manufacturer = ""
        main_office_adress1 = ""
        main_office_adress2 = ""
        main_office_name = ""
        contact_person_name = ""
        contact_person_phone = ""
        contact_person_email = ""
        manufacturers_has_cps_orders_key_list = []
        manufacturers_has_cps_orders_list = []
        manufacturers_manufacturer_id = ""
        storage_has_products_key_list = []

        suppliers_has_cps_orders_key_list = []
        suppliers_has_cps_orders = ""
        suppliers_supplier_id = ""
        cps_orders_internal_order_no = ""
        car_list_split = []
        car_manufacturer_list = []
        orders_order_no = 0
        products_product_id = 0
        manufacturer = ""
        color = ""
        year_model = ""
        owner_id = ""
        payment_date = ""
        payments_no = ""
        payment_amount = ""
        customer_paid_bill_id = ""
        my_first_name = ""
        my_last_names = ""
        my_street_adress = ""
        my_house_number = ""
        my_zip_code = ""
        my_city = ""
        my_country = ""
        my_company = ""
        my_phone = ""
        my_states = ""
        reg_no = ""
        colors = ""
        model = ""
        year = ""
        reg = ""
        date = ""
        street_adress = ""
        house_number = ""
        zip_code = ""
        city = ""
        country = ""
        company = ""
        phone = ""
        states = ""
        my_sales_representant = ""
        state = ""
        rnd_number = 0
        order_date = ""
        required_date = ""
        shipping_date = ""
        status = ""
        comments = ""
        customers_id_customers = ""
        order = ""
        productline = ""
        text_description = ""
        html_description = ""
        message = "saab.jpg"
        image = bytes(message, 'utf-8')
        products_copy_of_productlines_productline = ""
        product_name = ""
        product_description = ""
        inprice = ""
        outprice = ""
        productlines = ""
        product = ""
        order_no = 0
        quantity = 0
        price_each = 1.00
        orderdetails = ""
        staffs_has_cpsorders_key_list = []
        staffs_has_cpsorders = ""
        staffs_id_staff = ""
        cps_orders_internal_order_no = ""
        storage_has_products = ""
        storage_storage_id = 1
        products_product_id = 1
        staffs_has_staffs_key_list = []
        staffs_has_staffs = ""
        staffs_id_staff = ""
        staffs_id_staff1 = ""
        staffs_has_customers_key_list = []
        staffs_has_customers = ""
        staffs_id_staff = ""
        customers_id_customers = ""
        manufactureres_has_cps_orders_dict = ""
        manufactureres_has_cps_orders = ""
        storage_key_list = []
        staffs_has_cps_orders_key_list = []
        suppliers_contact_person = ""
        manufacturer_contact_person = ""

        # class selfs:

        # ORDER VARIABLES
        self.order = order
        self.order_date = order_date
        self.required_date = required_date
        self.shipping_date = shipping_date
        self.status = status
        self.comments = comments
        self.customers_id_customers = customers_id_customers
        self.order_no = order_no
        self.suppliers_supplier_id = suppliers_supplier_id
        self.cps_orders_internal_order_no = cps_orders_internal_order_no

        self.suppliers_has_cps_orders = suppliers_has_cps_orders
        self.name_manufacturer = name_manufacturer
        self.main_office_adress1 = main_office_adress1
        self.main_office_adress2 = main_office_adress2
        self.main_office_name = main_office_name
        self.contact_person_name = contact_person_name
        self.contact_person_phone = contact_person_phone
        self.contact_person_email = contact_person_email
        self.manufactureres_has_cps_orders = manufactureres_has_cps_orders

        self.manufacturers_manufacturer_id = manufacturers_manufacturer_id
        self.cps_orders_internal_order_no = cps_orders_internal_order_no

        self.manufacturers_has_cps_orders_list = manufacturers_has_cps_orders_list
        self.order_date = order_date
        self.required_date = required_date
        self.shipping_date = shipping_date
        self.status = status
        self.comments = comments
        self.order_no_comments = order_no_comments

        self.cps_orders = cps_orders

        self.staffs_id_staff = staffs_id_staff
        self.staffs_id_staff1 = staffs_id_staff1
        self.staffs_has_staffs_key_list = staffs_has_staffs_key_list
        self.staffs_has_staffs = staffs_has_staffs

        self.staffs_id_staff = staffs_id_staff
        self.cps_orders_internal_order_no = cps_orders_internal_order_no
        self.staffs_has_cpsorders_key_list = staffs_has_cpsorders_key_list
        self.staffs_has_cpsorders = staffs_has_cpsorders

        self.supplier_name = supplier_name
        self.supplier_adress1 = supplier_adress1
        self.supplier_adress2 = supplier_adress2
        self.city = city
        self.zip_code = zip_code
        self.country = country
        self.contact_person = contact_person
        self.phone_number = phone_number
        self.email = email

        self.suppliers = suppliers

        self.storage = storage
        self.storage_name = storage_name
        self.storage_quantity = storage_quantity
        self.storage_city = storage_city

        self.storage_storage_id = storage_storage_id
        self.products_product_id = products_product_id
        self.storage_has_products = storage_has_products

        self.manufactureres_has_cps_orders_dict = manufactureres_has_cps_orders_dict

        # PRODUCTLINES VARIABLES
        self.productline = productline
        self.text_description = text_description
        self.html_description = html_description
        self.image = image

        self.street_adress = street_adress
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.company = company
        self.phone = phone
        self.states = states
        self.car_list_split = car_list_split
        self.car_manufacturer_list = car_manufacturer_list
        self.manufacturer = manufacturer
        self.color = color
        self.year_model = year_model
        self.owner_id = owner_id
        self.payment_date = payment_date
        self.payments_no = payments_no
        self.payment_amount = payment_amount
        self.customer_paid_bill_id = customer_paid_bill_id
        self.my_first_name = my_first_name
        self.my_last_names = my_last_names
        self.my_street_adress = my_street_adress
        self.my_house_number = my_house_number
        self.my_zip_code = my_zip_code
        self.my_city = my_city
        self.my_country = my_country
        self.my_company = my_company
        self.my_phone = my_phone
        self.my_states = my_states
        self.reg_no = reg_no
        self.colors = colors
        self.model = model
        self.year = year
        self.reg = reg
        self.date = date
        self.generator = generator
        self.my_sales_representant = my_sales_representant
        self.state = state
        self.rnd_number = rnd_number
        self.products_copy_of_productlines_productline = products_copy_of_productlines_productline
        self.product_name = product_name
        self.product_description = product_description
        self.inprice = inprice
        self.outprice = outprice
        self.productlines = productlines
        self.product = product
        self.orders_order_no = orders_order_no
        self.products_product_id = products_product_id
        self.quantity = quantity
        self.price_each = price_each
        self.orderdetails = orderdetails
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.phone = phone
        self.reports_to = reports_to
        self.store = store
        self.staffs_key_list = staffs_key_list
        self.staffs = staffs
        self.storage_has_products_list = storage_has_products_list
        self.staffs_id_staff = staffs_id_staff
        self.customers_id_customers = customers_id_customers
        self.staffs_has_customers_key_list = staffs_has_customers_key_list
        self.staffs_has_customers = staffs_has_customers
        self.suppliers_contact_person = suppliers_contact_person
        self.manufacturer_contact_person = manufacturer_contact_person

        self.manufacturers = manufacturers

        self.supplier_name = supplier_name


        # KEY LISTS GOES HERE

        customer_key_list = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                             'city', 'zip_code', 'country', 'sales_representant', 'states']

        customer_car_key_list = ['reg_no', 'manufacturer', 'color', 'model', 'year_model', 'owner_id']

        payment_key_list = ['payment_date', 'payment_amount', 'customer_paid_bill_id']

        order_key_list = ['order_date', 'required_date', 'shipping_date', 'status', 'comments',
                          'customers_id_customers']

        productline_key_list = ['productline', 'text_description', 'html_description', 'image']

        product_key_list = ['product_name', 'product_description', 'inprice', 'outprice', 'productlines']

        orderdetails_key_list = ['orders_order_no', 'products_product_id', 'quantity', 'price_each']

        suppliers_has_cps_orders_key_list = ['suppliers_supplier_id', 'cps_orders_internal_order_no']

        manufacturers_key_list = ['name_manufacturer', 'main_office_adress1', 'main_office_adress2', 'main_office_name',
                                  'contact_person_name', 'contact_person_phone', 'contact_person_email']

        manufacturers_has_cps_orders_key_list = ['manufacturers_manufacturer_id', 'cps_orders_internal_order_no']

        staffs_key_list = ['first_name', 'last_name', 'job_title', 'phone', 'reports_to', 'store']

        cps_orders_key_list = ['order_date', 'required_date', 'shipping_date', 'status', 'comments',
                               'order_no_comments']

        staffs_has_cps_orders_key_list = ['staffs_id_staff', 'cps_orders_internal_order_no']

        suppliers_key_list = ['supplier_name', 'supplier_adress1', 'supplier_adress2', 'city', 'zip_code', 'country',
                              'contact_person', 'phone_number', 'email']

        storage_key_list = ['storage_name', 'storage_quantity', 'storage_city']

        storage_has_products_key_list = ['storage_storage_id', 'products_product_id']

        staffs_has_staffs_key_list = ['staffs_id_staff', 'staffs_id_staff1']

        staffs_has_customers_key_list = ['staffs_id_staff', 'customers_id_customers']

        self.customer_key_list = customer_key_list
        self.customer_car_key_list = customer_car_key_list
        self.payment_key_list = payment_key_list
        self.order_key_list = order_key_list
        self.productline_key_list = productline_key_list
        self.product_key_list = product_key_list
        self.orderdetails_key_list = orderdetails_key_list
        self.storage_key_list = storage_key_list
        self.suppliers_has_cps_orders_key_list = suppliers_has_cps_orders_key_list
        self.manufacturers_key_list = manufacturers_key_list
        self.manufacturers_has_cps_orders_key_list = manufacturers_has_cps_orders_key_list
        self.cps_orders_key_list = cps_orders_key_list
        self.staffs_key_list = staffs_key_list
        self.staffs_has_cps_orders_key_list = staffs_has_cps_orders_key_list
        self.suppliers_key_list = suppliers_key_list
        self.staffs_has_staffs_key_list = staffs_has_staffs_key_list
        self.storage_has_products_key_list = storage_has_products_key_list

        self.staffs_has_customers_key_list = staffs_has_customers_key_list

    def load_all_data(self):
        self.first_name = self.generator.load_first_name()
        self.last_name = self.generator.load_last_name()
        self.street_adress = self.generator.load_street_adress()
        self.house_number = self.generator.load_house_numbers()
        self.zip_code = self.generator.load_zip_codes()
        self.city = self.generator.load_citys()
        self.country = self.generator.load_country()
        self.company = self.generator.load_company()
        self.phone = self.generator.load_phone()
        self.states = self.generator.load_states()
        self.reg = self.generator.load_reg_no()
        self.colors = self.generator.load_color()
        self.model = self.generator.load_car_model()
        self.year = self.generator.load_year_model()
        self.date = self.generator.load_date()
        self.car_list_split, self.car_manufacturer_list = \
            self.generator.cars_and_their_manufacturers(self.car_list_split, self.car_manufacturer_list)
        self.reg_no = self.generator.reg_no_generator()
        self.status = self.generator.load_status()
        self.productline = self.generator.load_productline()
        self.text_description = self.generator.load_text_description()
        self.html_description = self.generator.load_html_description()
        self.image = self.generator.load_image()
        self.product_name = self.generator.load_product_name()
        self.product_description = self.generator.load_product_description()
        # self.inprice = self.generator.load_inprice()
        # self.outprice = self.generator.load_outprice()

    def assemble_customer_object(self):
        self.house_number = self.generator.create_house_number()
        self.first_name = self.generator.create_first_name()
        self.last_name = self.generator.create_last_name()
        self.company = self.generator.create_company()
        self.phone = self.generator.create_phone()
        self.street_adress = self.generator.create_street_adress()
        self.city = self.generator.create_city()
        self.zip_code = self.generator.create_zip_code()
        self.country = self.generator.create_country()
        self.my_sales_representant = self.generator.create_sales_representant()
        self.state = self.generator.create_states()

    def rnd_number_function(self):
        self.rnd_number = self.generator.random_customer_order_id()
        return self.rnd_number

    # HERE GOES ALL ASSEMBLE FUNCTIONS
    def assemble_car_object(self):
        self.reg_no = self.generator.random_reg_no()
        self.manufacturer = self.generator.random_manufacturer()
        self.color = self.generator.random_color()
        self.model = self.generator.random_car_model()
        self.year_model = self.generator.random_year_model()
        self.owner_id = self.generator.random_owner_id()

    def assemble_payment_object(self):
        self.payment_amount = self.generator.random_amount()
        self.payment_date = self.generator.random_date()
        self.customer_paid_bill_id = self.generator.random_payment_bill_id()

    def assemble_order_object(self):
        # self.order_no = cpsab.orders
        self.order_date = self.generator.random_date()
        self.required_date = self.generator.random_date()
        self.shipping_date = self.generator.random_date()
        self.status = self.generator.random_status()
        self.comments = ''
        self.customers_id_customers = self.rnd_number

    def assemble_productline_object(self):
        self.productline = self.generator.random_productline()
        self.text_description = self.generator.random_text_description()
        self.html_description = self.generator.random_html_description()
        self.image = self.generator.load_image()

        # self.generator.random_productline_image()
        # THIS ONE IS SPECIAL, HAS TO BE EXACT THE SAME IN THE PRODUCTS TABLE
        # OTHERWISE ITS GOING TO CRASH
        self.products_copy_of_productlines_productline = self.productline

    def assemble_products_object(self):
        self.product_name = self.generator.random_product_name()
        self.product_description = self.generator.random_product_descriptions()
        self.inprice = self.generator.random_inprice()
        self.outprice = self.generator.random_outprice()
        self.productlines = self.products_copy_of_productlines_productline

    def assemble_orderdetails_object(self):
        # här behöver vi hämta värden från dom snygga listorna, som Anna fixade.
        self.orders_order_no = self.orders_order_no = 3  # generator.random_orders_order_no()
        self.products_product_id = self.products_product_id = 1  # generator.random_products_product_id()
        self.quantity = self.generator.random_quantity()
        self.price_each = self.generator.random_price()

    # HERE GOES ALL DICT CREATING FUNCTIONS

    def create_customer_dict(self, customer_key_list, customer_list):
        self.customer = dict(zip(self.customer_key_list, customer_list))
        return self.customer

    def create_customer_car_dict(self, customer_car_key_list, customer_car_list):
        self.customer_car = dict(zip(self.customer_car_key_list, customer_car_list))
        return self.customer_car

    def create_payment_dict(self, payment_key_list, payment_list):
        self.payment = dict(zip(self.payment_key_list, payment_list))
        return self.payment

    def create_order_dict(self, order_key_list, order_list):
        self.order = dict(zip(self.order_key_list, order_list))
        return self.order

    def create_productline_dict(self, productline_key_list, productline_list):
        self.productline = dict(zip(self.productline_key_list, productline_list))
        return self.productline

    def create_product_dict(self, product_key_list, product_list):
        self.product = dict(zip(self.product_key_list, product_list))
        return self.product

    def create_orderdetails_dict(self, orderdetails_key_list, orderdetails_list):
        self.orderdetails = dict(zip(self.orderdetails_key_list, orderdetails_list))
        return self.orderdetails

    def create_suppliers_has_cps_orders_dict(self, suppliers_has_cps_orders_key_list, suppliers_has_cps_orders_list):
        self.suppliers_has_cps_orders = dict(zip(self.suppliers_has_cps_orders_key_list, suppliers_has_cps_orders_list))
        return self.suppliers_has_cps_orders

    def create_manufacturers_dict(self, manufacturers_id_key_list, manufacturers_list):
        self.manufacturers = dict(zip(self.manufacturers_key_list, manufacturers_list))
        return self.manufacturers

    def create_manufactureres_has_cps_orders_dict(self, manufactureres_has_cps_orders,
                                                  manufacturers_has_cps_orders_list):
        self.manufactureres_has_cps_orders = dict(
            zip(self.manufacturers_has_cps_orders_key_list, manufacturers_has_cps_orders_list))
        return self.manufactureres_has_cps_orders

    def create_staffs_dict(self, staffs_key_list, staffs_list):
        self.staffs = dict(zip(self.staffs_key_list, staffs_list))
        return self.staffs

    def create_cps_orders_dict(self, cps_orders_key_list, cps_orders_list):
        self.cps_orders = dict(zip(self.cps_orders_key_list, cps_orders_list))
        return self.cps_orders

    def create_staffs_has_cpsorders_dict(self, staffs_has_cpsorders_key_list, staffs_has_cpsorders_list):
        self.staffs_has_cpsorders = dict(zip(self.staffs_has_cpsorders_key_list, staffs_has_cpsorders_list))
        return self.staffs_has_cpsorders

    def create_suppliers_dict(self, suppliers_key_list, suppliers_list):
        self.suppliers = dict(zip(self.suppliers_key_list, suppliers_list))
        return self.suppliers

    def create_storage_dict(self, storage_key_list, storage_list):
        self.storage = dict(zip(self.storage_key_list, storage_list))
        return self.storage

    def create_storage_has_products_dict(self, storage_has_products_key_list, storage_has_products_list):
        self.storage_has_products = dict(zip(self.storage_has_products_key_list, storage_has_products_list))
        return self.storage_has_products

    def create_staffs_has_staffs_dict(self, staffs_has_staffs_key_list, staffs_has_staffs_list):
        self.staffs_has_staffs = dict(zip(self.staffs_has_staffs_key_list, staffs_has_staffs_list))
        return self.staffs_has_staffs

    def create_staffs_has_customers_dict(self, staffs_has_customers_key_list, staffs_has_customers_list):
        self.staffs_has_customers = dict(zip(self.staffs_has_customers_key_list, staffs_has_customers_list))
        return self.staffs_has_customers
