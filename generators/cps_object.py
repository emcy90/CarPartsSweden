import random

from app.bll.cps_orders_controller import get_cps_orders_by_id
from app.bll.customer_car_controller import get_customer_cars_by_reg_no
from app.bll.customer_controller import get_customer_by_id
from app.bll.manufacturer_controller import get_manufacturer_by_id
from app.bll.manufacturers_has_cps_orders_controller import get_manufacturer_has_cps_order_by_id
from app.bll.orderdetails_controller import get_order_details_by_id
from app.bll.payment_controller import get_payment_by_no
from app.bll.product_controller import get_product_by_id
from app.bll.productline_controller import get_productline_by_id
from app.bll.staff_has_customers_controller import get_staff_has_customer_by_id
from app.bll.staffs_has_cps_orders_controller import get_staff_has_cps_order_by_id
from app.bll.storage_controller import get_storage_by_id
from app.bll.storage_has_products_controller import get_storage_has_products_by_id
from app.bll.supplier_controller import get_supplier_by_id
from app.dll.repository.manufacturers_has_cps_orders_repository import get_manufacturer_cps_orders_internal_order_no
from app.dll.repository.order_repository import get_order_by_id
from app.dll.repository.orderdetails_repository import get_products_product_by_id
from app.dll.repository.staff_repository import get_staff_by_id
from app.dll.repository.staffs_has_cps_orders_repository import get_staffs_cps_orders_internal_order_no
from app.dll.repository.staffs_has_customers_repository import get_customers_id_customers_by_id, get_staffs_id_staffs
from app.dll.repository.storage_has_products_repository import get_storage_products_product_by_id
from app.dll.repository.suppliers_has_cps_orders_repository import get_suppliers_has_cps_order_by_id, \
    get_suppliers_cps_orders_internal_order_no
from generators.generator_setup import GeneratorSetup


class CpsCreator(GeneratorSetup):
    def __init__(self):
        super().__init__()

        # class variables:
        self.productlines_productline = None
        generator = GeneratorSetup()
        staffs_id_staff = ""
        all_cars_ids = []

        self.all_cps_order_ids = get_cps_orders_by_id()
        self.all_cars_ids = get_customer_cars_by_reg_no()
        self.all_customers_ids = get_customer_by_id()
        self.all_order_no = get_order_by_id()
        self.all_product_ids = get_product_by_id()
        self.all_payments_ids = get_payment_by_no()
        self.all_manufacturer_ids = get_manufacturer_by_id()
        self.all_manufacturer_cps_order_ids = get_manufacturer_has_cps_order_by_id()
        self.all_orderdetail_ids = get_order_details_by_id()
        self.all_productline_ids = get_productline_by_id()
        self.all_staff_ids = get_staff_by_id()
        self.all_staffs_cps_order_ids = get_staff_has_cps_order_by_id()
        self.all_staffs_has_customers_ids = get_staff_has_customer_by_id()
        self.all_customers_id_customers_ids = get_customers_id_customers_by_id()
        self.all_storage_has_products_ids = get_storage_has_products_by_id()
        self.all_storage_ids = get_storage_by_id()
        self.all_supplier_cps_orders_ids = get_suppliers_has_cps_order_by_id()
        self.all_supplier_ids = get_supplier_by_id()
        self.all_cps_order_internal_nos = get_cps_orders_by_id()
        self.all_manufacturer_cps_orders_internal_order_nos = get_manufacturer_cps_orders_internal_order_no()

        storage = ""
        storage_name = ""
        storage_quantity = ""
        storage_city = ""

        staffs_key_list = []
        all_products_product_ids = []
        staffs = ""
        first_name = ""
        last_name = ""
        job_title = ""
        reports_to = ""
        store = ""

        cps_orders = ""

        order_no_comments = ""
        suppliers = ""
        supplier_name = ""
        supplier_adress1 = ""
        supplier_adress2 = ""
        contact_person = ""
        phone_number = ""
        email = ""
        storage_has_products_list = []
        manufacturers = ""
        name_manufacturer = ""
        main_office_adress1 = ""
        main_office_adress2 = ""
        main_office_name = ""
        contact_person_name = ""
        contact_person_phone = ""
        contact_person_email = ""
        manufacturers_has_cps_orders_list = []
        suppliers_has_cps_orders = ""
        suppliers_supplier_id = ""
        cps_orders_internal_order_no = ""
        car_list_split = []
        car_manufacturer_list = []
        orders_order_no = 0
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
        all_staffs_staffs_ids = []
        all_suppliers_cps_orders_internal_nos_nos = []

        storage_has_products = ""
        storage_storage_id = 1
        products_product_id = 1

        staffs_has_customers_key_list = []
        staffs_has_customers = ""

        customers_id_customers = ""
        manufactureres_has_cps_orders = ""
        suppliers_contact_person = ""
        manufacturer_contact_person = ""
        staffs_has_cps_orders = ""
        copy_of_productline = ""
        copy_productline_from_products = ""
        copy_text_description = ""
        products_description_id = 0

        manufacturers_manufacturer_id = 0
        all_staffs_cps_orders_internal_order_no = []
        all_storage_products_product_ids = []
        super_mongo_customer_collection = []
        super_mongo_order_collection = []
        super_mongo_product_collection = []
        super_mongo_supplier_collection = []
        super_mongo_manufacturer_collection = []
        super_mongo_cps_orders_collection = []
        super_mongo_staff_collection = []
        super_mongo_storage_collection = []

        # class selfs:

        # ORDER VARIABEL
        self.all_storage_products_product_ids = all_storage_products_product_ids
        self.all_products_product_ids = all_products_product_ids
        self.all_staffs_cps_orders_internal_order_no = all_staffs_cps_orders_internal_order_no
        self.all_staffs_staffs_ids = all_staffs_staffs_ids

        self.order = order
        self.order_date = order_date
        self.required_date = required_date
        self.shipping_date = shipping_date
        self.status = status
        self.comments = comments
        self.customers_id_customers = customers_id_customers
        self.order_no = order_no
        self.suppliers_supplier_id = suppliers_supplier_id
        self.copy_productline_from_products = copy_productline_from_products
        self.suppliers_has_cps_orders = suppliers_has_cps_orders
        self.name_manufacturer = name_manufacturer
        self.main_office_adress1 = main_office_adress1
        self.main_office_adress2 = main_office_adress2
        self.main_office_name = main_office_name
        self.contact_person_name = contact_person_name
        self.contact_person_phone = contact_person_phone
        self.contact_person_email = contact_person_email
        self.manufactureres_has_cps_orders = manufactureres_has_cps_orders
        self.all_suppliers_cps_orders_internal_nos_nos = all_suppliers_cps_orders_internal_nos_nos

        self.manufacturers_has_cps_orders_list = manufacturers_has_cps_orders_list
        self.manufacturers_manufacturer_id = manufacturers_manufacturer_id
        self.order_date = order_date
        self.required_date = required_date
        self.shipping_date = shipping_date
        self.status = status
        self.comments = comments
        self.order_no_comments = order_no_comments

        self.cps_orders = cps_orders

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
        self.staffs_has_cps_orders = staffs_has_cps_orders

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
        self.customers_id_customers = customers_id_customers
        self.staffs_has_customers_key_list = staffs_has_customers_key_list
        self.staffs_has_customers = staffs_has_customers
        self.suppliers_contact_person = suppliers_contact_person
        self.manufacturer_contact_person = manufacturer_contact_person
        self.super_mongo_customer_collection = super_mongo_customer_collection
        self.manufacturers = manufacturers

        self.supplier_name = supplier_name
        self.date = date
        self.order_date = order_date
        self.staffs_id_staff = staffs_id_staff
        self.all_cars_ids = all_cars_ids
        self.copy_of_productline = copy_of_productline
        self.products_description_id = products_description_id
        self.super_mongo_order_collection = super_mongo_order_collection
        self.super_mongo_product_collection = super_mongo_product_collection
        self.super_mongo_supplier_collection = super_mongo_supplier_collection
        self.super_mongo_manufacturer_collection = super_mongo_manufacturer_collection
        self.super_mongo_cps_orders_collection = super_mongo_cps_orders_collection
        self.super_mongo_staff_collection = super_mongo_staff_collection
        self.super_mongo_storage_collection = super_mongo_storage_collection

        # KEY LISTS GOES HERE
        super_customer_key_list_mongo = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                                         'city', 'zip_code', 'country', 'sales_representant', 'states', 'reg_no',
                                         'manufacturer',
                                         'color', 'model', 'year_model', 'owner_id', 'payments_no', 'payment_date',
                                         'payment_amount', 'customer_paid_bill_id', 'staffs_id_staff',
                                         'customers_id_customers']

        super_order_key_list_mongo = ['order_no', 'order_date', 'required_date', 'shipping_date', 'status', 'comments',
                                      'customers_id_customers', 'orders_order_no', 'products_product_id', 'quantity',
                                      'price_each']

        super_product_key_list_mongo = ['product_id', 'product_name', 'product_description', 'inprice', 'outprice',
                                        'product_description', 'text_description', 'html_description', 'image',
                                        'products_description_id']

        super_supplier_key_list_mongo = ['supplier_id', 'supplier_name', 'supplier_adress1', 'supplier_adress2', 'city',
                                         'zip_code',
                                         'country',
                                         'contact_person', 'phone_number', 'email', 'suppliers_supplier_id',
                                         'cps_orders_internal_order_no']

        super_munufacturer_key_list_mongo = ['manufacturer_id', 'name_manufacturer', 'main_office_adress1',
                                             'main_office_adress2',
                                             'main_office_name',
                                             'contact_person_name', 'contact_person_phone', 'contact_person_email',
                                             'manufacturers_manufacturer_id', 'cps_orders_internal_order_no']

        super_cps_orders_key_list_mongo = ['internal_order_no', 'order_date', 'required_date', 'shipping_date',
                                           'status', 'comments',
                                           'order_no_comments', 'staffs_id_staff', 'cps_orders_internal_order_no']

        super_staff_key_list_mongo = ['id_staff', 'first_name', 'last_name', 'job_title', 'phone', 'store',
                                      'reports_to']

        super_storage_key_list_mongo = ['storage_id', 'storage_name', 'storage_quantity', 'storage_city',
                                        'storage_storage_id', 'products_product_id']

        customer_key_list = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                             'city', 'zip_code', 'country', 'sales_representant', 'states']

        customer_car_key_list = ['reg_no', 'manufacturer', 'color', 'model', 'year_model', 'owner_id']

        payment_key_list = ['payment_date', 'payment_amount', 'customer_paid_bill_id']

        order_key_list = ['order_date', 'required_date', 'shipping_date', 'status', 'comments',
                          'customers_id_customers']

        productline_key_list = ['product_description', 'text_description', 'html_description', 'image',
                                'products_description_id']

        product_key_list = ['product_name', 'product_description', 'inprice', 'outprice']

        orderdetails_key_list = ['orders_order_no', 'products_product_id', 'quantity', 'price_each']

        suppliers_has_cps_orders_key_list = ['suppliers_supplier_id', 'cps_orders_internal_order_no']

        manufacturers_key_list = ['name_manufacturer', 'main_office_adress1', 'main_office_adress2', 'main_office_name',
                                  'contact_person_name', 'contact_person_phone', 'contact_person_email']

        manufacturers_has_cps_orders_key_list = ['manufacturers_manufacturer_id', 'cps_orders_internal_order_no']

        cps_orders_key_list = ['order_date', 'required_date', 'shipping_date', 'status', 'comments',
                               'order_no_comments']

        staffs_has_cps_orders_key_list = ['staffs_id_staff', 'cps_orders_internal_order_no']

        suppliers_key_list = ['supplier_name', 'supplier_adress1', 'supplier_adress2', 'city', 'zip_code', 'country',
                              'contact_person', 'phone_number', 'email']

        storage_key_list = ['storage_name', 'storage_quantity', 'storage_city']

        storage_has_products_key_list = ['storage_storage_id', 'products_product_id']

        staffs_has_customers_key_list = ['staffs_id_staff', 'customers_id_customers']

        staffs_key_list = ['first_name', 'last_name', 'job_title', 'phone', 'store', 'reports_to']

        self.super_customer_key_list_mongo = super_customer_key_list_mongo
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
        self.storage_has_products_key_list = storage_has_products_key_list

        self.staffs_has_customers_key_list = staffs_has_customers_key_list

        self.cps_orders_internal_order_no = cps_orders_internal_order_no
        self.copy_text_description = copy_text_description
        self.super_customer_key_list_mongo = super_customer_key_list_mongo
        self.super_order_key_list_mongo = super_order_key_list_mongo
        self.super_product_key_list_mongo = super_product_key_list_mongo
        self.super_supplier_key_list_mongo = super_supplier_key_list_mongo
        self.super_munufacturer_key_list_mongo = super_munufacturer_key_list_mongo
        self.super_cps_orders_key_list_mongo = super_cps_orders_key_list_mongo
        self.super_staff_key_list_mongo = super_staff_key_list_mongo
        self.super_storage_key_list_mongo = super_storage_key_list_mongo

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

    # HERE GOES ALL ASSEMBLE FUNCTIONS
    def assemble_car_object(self, all_cars_ids):
        self.all_cars_ids = get_customer_cars_by_reg_no()

        self.reg_no = self.generator.random_reg_no()
        if self.reg_no in self.all_cars_ids:
            status = True
            while status:
                self.all_cars_ids = get_customer_cars_by_reg_no()
                # print("Reg number exists, generating a new one: ")
                self.reg_no = self.generator.random_reg_no()
                if self.reg_no not in self.all_cars_ids:
                    status = False
                    self.manufacturer = self.generator.random_manufacturer()
                    self.color = self.generator.random_color()
                    self.model = self.generator.random_car_model()
                    self.year_model = self.generator.random_year_model()
                    self.owner_id = random.choice(self.all_customers_ids)
                    self.all_cars_ids = get_customer_cars_by_reg_no()
        else:

            self.manufacturer = self.generator.random_manufacturer()
            self.color = self.generator.random_color()
            self.model = self.generator.random_car_model()
            self.year_model = self.generator.random_year_model()
            self.owner_id = random.choice(self.all_customers_ids)
            self.all_cars_ids = get_customer_cars_by_reg_no()

    def assemble_payment_object(self):
        self.payment_amount = self.generator.random_amount()
        self.payment_date = self.generator.random_date()
        self.customer_paid_bill_id = random.choice(self.all_customers_ids)

    def assemble_order_object(self):
        self.order_date = self.generator.random_date()
        self.required_date = self.generator.random_date()
        self.shipping_date = self.generator.random_date()
        self.status = self.generator.random_status()
        self.comments = ''
        self.customers_id_customers = random.choice(self.all_customers_ids)

    def assemble_productline_object(self):
        self.all_product_ids = get_product_by_id()
        self.product_description = self.generator.random_productline()
        self.text_description = self.generator.random_text_description()
        self.html_description = self.generator.random_html_description()
        self.image = self.generator.load_image()
        self.products_description_id = self.all_product_ids[-1]
        print()
        # THIS ONE IS SPECIAL, HAS TO BE EXACT THE SAME IN THE PRODUCTS TABLE
        # OTHERWISE ITS GOING TO CRASH

    def assemble_products_object(self):
        self.product_name = self.generator.random_product_name()
        self.product_description = self.generator.random_product_descriptions()
        self.inprice = self.generator.random_inprice()
        self.outprice = self.generator.random_outprice()

    def assemble_orderdetails_object(self):
        real_product_id_and_order_no_list = []
        self.all_order_no = get_order_by_id()
        self.all_product_ids = get_product_by_id()

        self.all_orderdetail_ids = get_order_details_by_id()
        self.all_products_product_ids = get_products_product_by_id()

        for xx in range(len(self.all_orderdetail_ids)):
            st1 = self.all_orderdetail_ids[xx]
            cu1 = self.all_products_product_ids[xx]
            real_product_id_and_order_no_list.append([st1, cu1])

        last_orderdetail_id = self.all_order_no[-1]
        last_product_rnd_id = self.all_product_ids[-1]
        lokal_orderdetail_id = random.randint(1, last_orderdetail_id)
        lokal_product_id = random.randint(1, last_product_rnd_id)

        orderdetails_product_combo_list = [lokal_orderdetail_id, lokal_product_id]

        if orderdetails_product_combo_list not in real_product_id_and_order_no_list:
            real_product_id_and_order_no_list.append(orderdetails_product_combo_list)
            variable_to_split_list = real_product_id_and_order_no_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.orders_order_no = x
            self.products_product_id = y

        else:
            loop = True
            while loop:
                last_orderdetail_id = self.all_order_no[-1]
                last_product_rnd_id = self.all_product_ids[-1]
                lokal_orderdetail_id = random.randint(1, last_orderdetail_id)
                lokal_product_id = random.randint(1, last_product_rnd_id)

                orderdetails_product_combo_list = [lokal_orderdetail_id, lokal_product_id]

                if orderdetails_product_combo_list not in real_product_id_and_order_no_list:
                    real_product_id_and_order_no_list.append(orderdetails_product_combo_list)
                    variable_to_split_list = real_product_id_and_order_no_list[-1]

                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.orders_order_no = x
                    self.products_product_id = y
                    loop = False

        self.quantity = self.generator.random_quantity()
        self.price_each = self.generator.random_price()

    def assemble_storage_object(self):
        storage_name_list = ['lager g??teborg', 'lager stockholm', 'lager malm??']
        quantity_list = [12, 43, 64, 2, 5]
        self.storage_name = random.choice(storage_name_list)
        self.storage_quantity = random.choice(quantity_list)
        self.storage_city = self.generator.create_city()

    def assemble_storage_has_products_object(self):
        real_storage_id_and_product_id_list = []

        self.all_storage_ids = get_storage_by_id()
        self.all_product_ids = get_product_by_id()

        self.all_storage_has_products_ids = get_storage_has_products_by_id()
        self.all_storage_products_product_ids = get_storage_products_product_by_id()

        for xx in range(len(self.all_storage_has_products_ids)):
            st1 = self.all_storage_has_products_ids[xx]
            cu1 = self.all_storage_products_product_ids[xx]
            real_storage_id_and_product_id_list.append([st1, cu1])

        last_storage_id = self.all_storage_ids[-1]
        last_product_id = self.all_product_ids[-1]

        lokal_storage_id = random.randint(1, last_storage_id)
        lokal_product_id = random.randint(1, last_product_id)

        storage_product_combo_list = [lokal_storage_id, lokal_product_id]

        if storage_product_combo_list not in real_storage_id_and_product_id_list:
            real_storage_id_and_product_id_list.append(storage_product_combo_list)
            variable_to_split_list = real_storage_id_and_product_id_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.storage_storage_id = x
            self.products_product_id = y

        else:
            loop = True
            while loop:
                last_storage_id = self.all_storage_ids[-1]
                last_product_id = self.all_product_ids[-1]

                lokal_storage_id = random.randint(1, last_storage_id)
                lokal_product_id = random.randint(1, last_product_id)

                storage_product_combo_list = [lokal_storage_id, lokal_product_id]

                if storage_product_combo_list not in real_storage_id_and_product_id_list:
                    real_storage_id_and_product_id_list.append(storage_product_combo_list)
                    variable_to_split_list = real_storage_id_and_product_id_list[-1]

                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.storage_storage_id = x
                    self.products_product_id = y
                    loop = False

    def assemble_supplier_object(self):
        suppliers = ['johans verkstad', 'biltema', 'jula']
        self.supplier_name = random.choice(suppliers)
        self.supplier_adress1 = self.generator.create_street_adress()
        self.supplier_adress2 = ""
        self.city = self.generator.create_city()
        self.zip_code = self.generator.create_zip_code()
        self.country = self.generator.create_country()

        self.suppliers_contact_person = self.generator.random_first_and_last_name()
        self.phone_number = self.generator.create_phone()
        self.email = self.generator.generate_random_email(self.suppliers_contact_person)

    def assemble_cps_orders_object(self):
        self.order_date = self.generator.random_date()
        self.required_date = self.generator.random_date()
        self.shipping_date = self.generator.random_date()
        self.status = self.generator.random_status()
        self.comments = ""
        self.order_no_comments = ""

    def assemble_suppliers_has_cps_orders_object(self):
        real_supplier_id_and_internal_order_no_list = []

        self.all_supplier_ids = get_supplier_by_id()
        self.all_cps_order_ids = get_cps_orders_by_id()

        self.all_supplier_cps_orders_ids = get_suppliers_has_cps_order_by_id()
        self.all_suppliers_cps_orders_internal_nos_nos = get_suppliers_cps_orders_internal_order_no()

        for xx in range(len(self.all_supplier_cps_orders_ids)):
            st1 = self.all_supplier_cps_orders_ids[xx]
            cu1 = self.all_suppliers_cps_orders_internal_nos_nos[xx]
            real_supplier_id_and_internal_order_no_list.append([st1, cu1])

        last_supplier_id = self.all_supplier_ids[-1]
        last_internal_order_no = self.all_cps_order_ids[-1]

        lokal_supplier_id = random.randint(1, last_supplier_id)
        lokal_internal_order_no = random.randint(1, last_internal_order_no)

        supplier_internal_order_combo_list = [lokal_supplier_id, lokal_internal_order_no]

        if supplier_internal_order_combo_list not in real_supplier_id_and_internal_order_no_list:
            real_supplier_id_and_internal_order_no_list.append(supplier_internal_order_combo_list)
            variable_to_split_list = real_supplier_id_and_internal_order_no_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.suppliers_supplier_id = x
            self.cps_orders_internal_order_no = y

        else:
            loop = True
            while loop:
                last_supplier_id = self.all_supplier_ids[-1]
                last_internal_order_no = self.all_cps_order_ids[-1]

                lokal_supplier_id = random.randint(1, last_supplier_id)
                lokal_internal_order_no = random.randint(1, last_internal_order_no)

                supplier_internal_order_combo_list = [lokal_supplier_id, lokal_internal_order_no]

                if supplier_internal_order_combo_list not in real_supplier_id_and_internal_order_no_list:
                    real_supplier_id_and_internal_order_no_list.append(supplier_internal_order_combo_list)
                    variable_to_split_list = real_supplier_id_and_internal_order_no_list[-1]

                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.suppliers_supplier_id = x
                    self.cps_orders_internal_order_no = y
                    loop = False

    def assemble_manufacturers_object(self):
        self.name_manufacturer = self.generator.random_manufacturer()
        self.main_office_adress1 = self.generator.create_street_adress()
        self.main_office_adress2 = ""
        main_office_name_rnd = ['G??teborgs kontoret', 'Falkenberg kontoret', 'Stockholms kontoret', 'Varbers kontoret']
        self.main_office_name = random.choice(main_office_name_rnd)
        self.manufacturer_contact_person = self.generator.random_first_and_last_name()
        self.contact_person_phone = self.generator.create_phone()
        self.contact_person_email = self.generator.generate_random_email(self.manufacturer_contact_person)

    def assemble_manufacturers_has_cps_orders_object(self):
        real_manufacturer_id_and_internal_order_no_list = []

        self.all_manufacturer_ids = get_manufacturer_by_id()
        self.all_cps_order_ids = get_cps_orders_by_id()

        self.all_manufacturer_cps_order_ids = get_manufacturer_has_cps_order_by_id()
        self.all_manufacturer_cps_orders_internal_order_nos = get_manufacturer_cps_orders_internal_order_no()

        for xx in range(len(self.all_manufacturer_cps_order_ids)):
            st1 = self.all_manufacturer_cps_order_ids[xx]
            cu1 = self.all_manufacturer_cps_orders_internal_order_nos[xx]
            real_manufacturer_id_and_internal_order_no_list.append([st1, cu1])

        last_manufacturer_id = self.all_manufacturer_ids[-1]
        last_manu_internal_order_no = self.all_cps_order_ids[-1]

        lokal_manufacturer_id = random.randint(1, last_manufacturer_id)
        lokal_manu_internal_order_no = random.randint(1, last_manu_internal_order_no)

        manufacturer_internal_order_combo_list = [lokal_manufacturer_id, lokal_manu_internal_order_no]

        if manufacturer_internal_order_combo_list not in real_manufacturer_id_and_internal_order_no_list:
            real_manufacturer_id_and_internal_order_no_list.append(manufacturer_internal_order_combo_list)
            variable_to_split_list = real_manufacturer_id_and_internal_order_no_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.manufacturers_manufacturer_id = x
            self.cps_orders_internal_order_no = y

        else:
            loop = True
            while loop:
                last_manufacturer_id = self.all_manufacturer_ids[-1]
                last_manu_internal_order_no = self.all_cps_order_ids[-1]

                lokal_manufacturer_id = random.randint(1, last_manufacturer_id)
                lokal_manu_internal_order_no = random.randint(1, last_manu_internal_order_no)

                manufacturer_internal_order_combo_list = [lokal_manufacturer_id, lokal_manu_internal_order_no]

                if manufacturer_internal_order_combo_list not in real_manufacturer_id_and_internal_order_no_list:
                    real_manufacturer_id_and_internal_order_no_list.append(manufacturer_internal_order_combo_list)
                    variable_to_split_list = real_manufacturer_id_and_internal_order_no_list[-1]

                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.manufacturers_manufacturer_id = x
                    self.cps_orders_internal_order_no = y
                    loop = False

    def assemble_staffs_object(self):
        self.first_name = self.generator.create_first_name()
        self.last_name = self.generator.create_last_name()
        job_title_list = ['salesperson', 'orderhandler', 'ceo', 'customer manager relations', 'sales manager',
                          'account manager']
        self.job_title = random.choice(job_title_list)
        self.phone = self.generator.create_phone()
        store_list = ['CPS Stockholm', 'CPS G??teborg', 'CPS Malm??', 'CPS Norrk??ping', 'CPS Link??ping', 'CPS ??rebro',
                      'CPS Sk??vde']
        self.store = random.choice(store_list)
        self.reports_to = random.choice(self.all_staff_ids)

    def assemble_staffs_has_cps_orders_object(self):
        st1 = ""
        cu = ""

        real_staff_and_cps_internal_order_no_list = []
        self.all_staff_ids = get_staff_by_id()
        self.all_cps_order_ids = get_cps_orders_by_id()

        self.all_staffs_cps_order_ids = get_staff_has_cps_order_by_id()
        self.all_staffs_cps_orders_internal_order_no = get_staffs_cps_orders_internal_order_no()

        for xx in range(len(self.all_staffs_cps_order_ids)):
            st1 = self.all_staffs_cps_order_ids[xx]
            cu1 = self.all_staffs_cps_orders_internal_order_no[xx]
            real_staff_and_cps_internal_order_no_list.append([st1, cu1])

        last_cps_order_internal_no = self.all_cps_order_ids[-1]
        # will crash in the beginning a bit until you have 6 in staff
        lokal_staff_id = random.randint(1, 6)
        random_cps_order_internal_no = random.randint(1, last_cps_order_internal_no)

        staff_internal_no_order_combo_list = [lokal_staff_id, random_cps_order_internal_no]

        if staff_internal_no_order_combo_list not in real_staff_and_cps_internal_order_no_list:
            real_staff_and_cps_internal_order_no_list.append(staff_internal_no_order_combo_list)
            variable_to_split_list = real_staff_and_cps_internal_order_no_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.staffs_id_staff = x
            self.cps_orders_internal_order_no = y

        else:
            loop = True
            while loop:
                last_cps_order_internal_no = self.all_cps_order_ids[-1]
                lokal_staff_id = random.randint(1, 6)
                random_cps_order_internal_no = random.randint(1, last_cps_order_internal_no)
                staff_internal_no_order_combo_list = [lokal_staff_id, random_cps_order_internal_no]

                if staff_internal_no_order_combo_list not in real_staff_and_cps_internal_order_no_list:
                    real_staff_and_cps_internal_order_no_list.append(staff_internal_no_order_combo_list)
                    variable_to_split_list = real_staff_and_cps_internal_order_no_list[-1]

                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.staffs_id_staff = x
                    self.cps_orders_internal_order_no = y
                    loop = False

    def assemble_staffs_has_customers_object(self):
        real_staff_and_customer_id_list = []

        self.all_staff_ids = get_staff_by_id()
        self.all_customers_ids = get_customer_by_id()

        self.all_staffs_staffs_ids = get_staffs_id_staffs()
        self.all_customers_id_customers_ids = get_customers_id_customers_by_id()

        for xx in range(len(self.all_staffs_staffs_ids)):
            st1 = self.all_staffs_staffs_ids[xx]
            cu1 = self.all_customers_id_customers_ids[xx]
            real_staff_and_customer_id_list.append([st1, cu1])

        last_customer_id = self.all_customers_ids[-1]
        lokal_staff_id = random.randint(1, 6)
        random_customer_id = random.randint(1, last_customer_id)

        staff_customer_combo_list = [lokal_staff_id, random_customer_id]

        if staff_customer_combo_list not in real_staff_and_customer_id_list:
            real_staff_and_customer_id_list.append(staff_customer_combo_list)
            variable_to_split_list = real_staff_and_customer_id_list[-1]

            cc = str(variable_to_split_list)
            cc = cc.replace('[', '')
            cc = cc.replace(']', '')
            cc = cc.strip()

            x, y = cc.split(',')
            x = (int(x))
            y = (int(y))
            self.staffs_id_staff = x
            self.customers_id_customers = y

        else:
            loop = True
            while loop:
                last_customer_id = self.all_customers_ids[-1]
                lokal_staff_id = random.randint(1, 6)
                random_customer_id = random.randint(1, last_customer_id)

                staff_customer_combo_list = [lokal_staff_id, random_customer_id]

                if staff_customer_combo_list not in real_staff_and_customer_id_list:
                    real_staff_and_customer_id_list.append(staff_customer_combo_list)
                    variable_to_split_list = real_staff_and_customer_id_list[-1]
                    cc = str(variable_to_split_list)
                    cc = cc.replace('[', '')
                    cc = cc.replace(']', '')
                    cc = cc.strip()

                    x, y = cc.split(',')
                    x = (int(x))
                    y = (int(y))
                    self.staffs_id_staff = x
                    self.customers_id_customers = y
                    loop = False

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

    def create_staffs_has_cps_orders_dict(self, staffs_has_cps_orders_key_list, staffs_has_cps_orders_list):
        self.staffs_has_cpsorders = dict(zip(self.staffs_has_cps_orders_key_list, staffs_has_cps_orders_list))
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

    def create_staffs_has_customers_dict(self, staffs_has_customers_key_list, staffs_has_customers_list):
        self.staffs_has_customers = dict(zip(self.staffs_has_customers_key_list, staffs_has_customers_list))
        return self.staffs_has_customers

    def create_super_customer_mongo_dict(self, super_customer_key_list_mongo, customer_list):
        self.super_mongo_customer_collection = dict(zip(super_customer_key_list_mongo, customer_list))
        return self.super_mongo_customer_collection

    def create_super_order_mongo_dict(self, super_order_key_list_mongo, order_list):
        self.super_mongo_order_collection = dict(zip(super_order_key_list_mongo, order_list))
        return self.super_mongo_order_collection

    def create_super_product_mongo_dict(self, super_product_key_list_mongo, product_list):
        self.super_mongo_product_collection = dict(zip(super_product_key_list_mongo, product_list))
        return self.super_mongo_product_collection

    def create_super_supplier_mongo_dict(self, super_supplier_key_list_mongo, supplier_list):
        self.super_mongo_supplier_collection = dict(zip(super_supplier_key_list_mongo, supplier_list))
        return self.super_mongo_supplier_collection

    def create_super_munufacturer_mongo_dict(self, super_munufacturer_key_list_mongo, mongo_creator_manufacturer_list):
        self.super_mongo_manufacturer_collection = dict(zip(super_munufacturer_key_list_mongo,
                                                            mongo_creator_manufacturer_list))
        return self.super_mongo_manufacturer_collection

    def create_super_cps_orders_mongo_dict(self, super_cps_orders_key_list_mongo, mongo_creator_cps_order_list):
        self.super_mongo_cps_orders_collection = dict(zip(super_cps_orders_key_list_mongo,
                                                          mongo_creator_cps_order_list))
        return self.super_mongo_cps_orders_collection

    def create_super_staff_mongo_dict(self, super_staff_key_list_mongo, mongo_creator_staff_list):
        self.super_mongo_staff_collection = dict(zip(super_staff_key_list_mongo,
                                                     mongo_creator_staff_list))
        return self.super_mongo_staff_collection

    def create_super_storage_mongo_dict(self, super_storage_key_list_mongo, mongo_creator_storage_list):
        self.super_mongo_storage_collection = dict(zip(super_storage_key_list_mongo,
                                                       mongo_creator_storage_list))
        return self.super_mongo_storage_collection
