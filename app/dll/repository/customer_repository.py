from bson import ObjectId

from app.dll.db import session
from app.dll.models import Customer, CustomerCar

from app.view import main

from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


def get_customer_by_id():
    customer_id = session.query(Customer.id_customers).all()
    customer_id_clean_list = []
    for id in customer_id:
        customer_id_clean_list.append(id[0])
    return customer_id_clean_list


# def show_one_customer_example_of_car():
    # this is just an example
    # show_customers = session.query(Customer).all()
    # count = 0
    # for customers in show_customers:
    #     xc = len(customers.customer_cars)
    #     print(customers.customer_cars[count].color)
    #     if count == xc:
    #         count = 0

    #   print(
    #      f'Customer id: {customers.id_customers} First name: {customers.first_name} Last name: {customers.last_name}')


def show_one_customer(xxx):
    all_customers = session.query(Customer.id_customers).all()
    all_customer_ids_clean_list = []
    for id in all_customers:
        all_customer_ids_clean_list.append(id[0])

    up_customer = session.query(Customer).filter(Customer.id_customers == xxx).first()
    if up_customer is None:
        print("This person id, does not exists:")
        main()
    else:

        print(f' Customer id: {up_customer.id_customers}\n First name: {up_customer.first_name}\n'
              f' Last name: {up_customer.last_name}\n Company name: {up_customer.company_name}\n'
              f' Phone: {up_customer.phone}\n Adress 1: {up_customer.adress1}\n Adress 2: {up_customer.adress2}\n',
              f'City: {up_customer.city}\n Zipcode: {up_customer.zip_code}\n'
              f' Country: {up_customer.country}\n sales_representant: {up_customer.sales_representant}\n'
              f' State: {up_customer.states}')
        print()
        print('*******************************************************************')


def show_all_customers():
    show_customers = session.query(Customer).all()

    for show_cust in show_customers:
        print(f' Customer id: {show_cust.id_customers}\n First name: {show_cust.first_name}\n'
              f' Last name: {show_cust.last_name}\n Company name: {show_cust.company_name}\n'
              f' Phone: {show_cust.phone}\n Adress 1: {show_cust.adress1}\n Adress 2: {show_cust.adress2}\n',
              f'City: {show_cust.city}\n Zipcode: {show_cust.zip_code}\n'
              f' Country: {show_cust.country}\n sales_representant: {show_cust.sales_representant}\n'
              f' State: {show_cust.states}')
        print()
        print('*******************************************************************')


def delete_customer(xxx):
    del_customer2 = session.query(Customer).filter(Customer.id_customers == xxx).first()
    if del_customer2 is None:
        print("Cannot delete, the person doesnt exist.")
        main()
    else:

        print(del_customer2)

        print(del_customer2.id_customers)
        print(f'Customer id: {del_customer2.id_customers}\nFirst Name: {del_customer2.first_name}\n'
              f'Last Name: {del_customer2.last_name}\nCompany Name: {del_customer2.company_name}'
              f'\nPhone: {del_customer2.phone}\nAddress 1: {del_customer2.adress1}\n'
              f'Adress 2: {del_customer2.adress2}\nCity: {del_customer2.city}\n'
              f'Zip Code: {del_customer2.zip_code}\nCountry: {del_customer2.country}\n'
              f'Sales_representant: {del_customer2.sales_representant}\nState: {del_customer2.states}')

        xx = str(input("Do you want to delete this customer? Please type y for yes if you want to proceed "))

        if xx[0] == "y":
            session.query(Customer).filter(Customer.id_customers == xxx).delete()

            session.commit()
            print(f'customer deleted')
        else:
            main()


def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
    print()
    print('Added customer successfully.')


def mongo_create_customer(mongo_customer):
    my_clean_dict = mongo_customer

    print()
    db.customers.insert_one(my_clean_dict)
    print("Added mongo customer")


def update_customer(xxx):
    running = True

    while running:
        up_customer = session.query(Customer).filter(Customer.id_customers == xxx).first()
        if up_customer is None:
            print("Cannot update, the person doesnt exist.")
            main()
        else:
            print(f' Customer id: {up_customer.id_customers}\n First name: {up_customer.first_name}\n'
                  f' Last name: {up_customer.last_name}\n Company name: {up_customer.company_name}\n'
                  f' Phone: {up_customer.phone}\n Adress 1: {up_customer.adress1}\n Adress 2: {up_customer.adress2}\n',
                  f'City: {up_customer.city}\n Zipcode: {up_customer.zip_code}\n'
                  f' Country: {up_customer.country}\n sales_representant: {up_customer.sales_representant}\n'
                  f' State: {up_customer.states}')
            print()
            print('*******************************************************************')

            print("Press (1) for update first name")
            print("Press (2) for update last name")
            print("Press (3) for update company name")
            print("Press (4) for update phone")
            print("Press (5) for update adress 1")
            print("Press (6) for update adress 2")
            print("Press (7) for update city")
            print("Press (8) for update zip code")
            print("Press (9) for update country")
            print("Press (10) for update sales_representant")
            print("Press (11) for update state")
            valet = str(input('Press number to update: '))

            if valet == "1":
                up_customer.first_name = str(input('Enter new first_name: '))
                session.commit()
                print("Updated first name field")

            elif valet == "2":
                up_customer.last_name = str(input('Enter new last_name: '))
                session.commit()
                print("Updated last name field")

            elif valet == "3":
                up_customer.company_name = str(input('Enter new company_name: '))
                session.commit()
                print("Updated company field.")

            elif valet == "4":
                up_customer.phone = str(input('Enter new phone: '))
                session.commit()
                print("Updated phone field.")

            elif valet == "5":
                up_customer.adress1 = str(input('Enter new adress1: '))
                session.commit()
                print("Updated adress 1 field.")

            elif valet == "6":
                up_customer.adress2 = str(input('Enter new adress2: '))
                session.commit()
                print("Updated adress 2 field.")

            elif valet == "7":
                up_customer.city = str(input('Enter new city: '))
                session.commit()
                print("Updated city field.")

            elif valet == "8":
                up_customer.zip_code = str(input('Enter new zip code: '))
                session.commit()
                print("Updated zip code field.")

            elif valet == "9":
                up_customer.country = str(input('Enter new country: '))
                session.commit()
                print("Updated country field")

            elif valet == "10":
                up_customer.sales_representant = str(input('Enter new sales representant: '))
                session.commit()
                print("Updated sales representant field")

            elif valet == "11":
                up_customer.state = str(input('Enter new state: '))
                session.commit()
                print("Updated state field")

            up_customer = session.query(Customer).filter(Customer.id_customers == xxx).first()

            print(f' Customer id: {up_customer.id_customers}\n First name: {up_customer.first_name}\n'
                  f' Last name: {up_customer.last_name}\n Company name: {up_customer.company_name}\n'
                  f' Phone: {up_customer.phone}\n Adress 1: {up_customer.adress1}\n Adress 2: {up_customer.adress2}\n',
                  f'1City: {up_customer.city}\n Zipcode: {up_customer.zip_code}\n'
                  f' Country: {up_customer.country}\n sales_representant: {up_customer.sales_representant}\n'
                  f' State: {up_customer.states}')
            print()

            sista_valet = str(input('Are you finished updating? (yes/no)? '))
            if sista_valet[0] == "y":
                running = False
                main()
            else:
                continue


def view_single_mongo_customer(xxx):
    id_finder2 = db.customers.find({"_id": ObjectId(xxx)})

    for mongo_customer in id_finder2:
        obj_id = (mongo_customer['_id'])
        first_name = (mongo_customer['first_name'])  # ['_id'])
        last_name = (mongo_customer['last_name'])
        company_name = (mongo_customer['company_name'])
        phone = (mongo_customer['phone'])
        adress1 = (mongo_customer['adress1'])
        adress2 = (mongo_customer['adress2'])
        city = (mongo_customer['city'])
        zip_code = (mongo_customer['zip_code'])
        country = (mongo_customer['country'])
        sales_representant = (mongo_customer['sales_representant'])
        states = (mongo_customer['states'])
        print(f'\nObjectId {obj_id}\nFirst Name: {first_name}\n'
              f'Last Name: {last_name}\nCompany Name: {company_name}\nPhone: {phone}\n'
              f'Address: {adress1}\nAddress 2: {adress2}\nCity: {city}\nZip Code: {zip_code}\nCountry: {country}\n'
              f'Sales Representant: {sales_representant}\nState: {states}')

    car_finder = db.customers.find({"owner_id": ObjectId(xxx)})
    car_records = list(car_finder)
    if len(car_records) == 0:
        print("This customer dont have any cars.")
        reg_no = ""
        manufacturer = ""
        color = ""
        model = ""
        year_model = ""
        owner_id = ""

    else:

        # Create a number of cars list the person has.
        number_of_cars_found_list = []
        print()
        print(f"Cars who customer: {first_name} {last_name}")
        print()
        for m1 in car_records:
            reg_no = (m1['reg_no'])
            manufacturer = (m1['manufacturer'])
            color = (m1['color'])
            model = (m1['model'])
            year_model = (m1['year_model'])
            owner_id = (m1['owner_id'])
            number_of_cars_found_list.append(reg_no)

            print(f'reg no: {reg_no}\nmanufacturer {manufacturer}\n'
                  f'color: {color}\nModel: {model}\nyear model: {year_model}\nowner id: {owner_id}\n')

        # Here we get the customer payments
        payment_finder = db.customers.find(({"customer_paid_bill_id": ObjectId(xxx)}))
        payment_records = list(payment_finder)
        if len(payment_records) == 0:
            print("This customer dont have any payments")
            payments_no = ""
            payment_date = ""
            payment_amount = ""
            customer_paid_bill_id = ""
        else:
            collected_paid_bills_id = []
            print()
            print(f"Customers Payments: {first_name} {last_name}")
            print()
            for m2 in payment_records:
                payments_no = (m2['payments_no'])
                payment_date = (m2['payment_date'])
                payment_amount = (m2['payment_amount'])
                customer_paid_bill_id = (m2['customer_paid_bill_id'])
                collected_paid_bills_id.append(payments_no)
            num_payments = len(collected_paid_bills_id)

            print(f'payments no: {payments_no}\n'
                  f'payment date: {payment_date}\npayment amount: {payment_amount}\n'
                  f'customer paid bill id: {customer_paid_bill_id}')

            # Here we get customer staffs
            staff_finder = db.customers.find(({"customers_id_customers": ObjectId(xxx)}))
            staff_records = list(staff_finder)
            if len(staff_records) == 0:
                print("This customer doesnt have any staff.")
                staffs_id_staff = ""
                customers_id_customers = ""

            else:
                our_sales_personal = []
                print()
                print(f"Customers Staff: {first_name} {last_name}")
                print()
                for m3 in staff_records:
                    staffs_id_staff = (m3['staffs_id_staff'])
                    customers_id_customers = (m3['customers_id_customers'])
                    our_sales_personal.append(staffs_id_staff)
                num_staff = len(our_sales_personal)

                print(f'staff id staff: {staffs_id_staff}\ncustomers id customers: {customers_id_customers}')


def view_all_mongo_customers():
    id_items = db.customers.find()

    filtered = []
    for item in id_items:

        # checking the cursor object so it has all these attributes.
        # so we can handle the program not to crash, if one is missing.
        if 'first_name' and 'company_name' in item:

            filtered.append(item)

            for mongo_customer in filtered:
                obj_id = (mongo_customer['_id'])
                first_name = (mongo_customer['first_name'])  # ['_id'])
                last_name = (mongo_customer['last_name'])
                company_name = (mongo_customer['company_name'])
                phone = (mongo_customer['phone'])
                adress1 = (mongo_customer['adress1'])
                adress2 = (mongo_customer['adress2'])
                city = (mongo_customer['city'])
                zip_code = (mongo_customer['zip_code'])
                country = (mongo_customer['country'])
                sales_representant = (mongo_customer['sales_representant'])
                states = (mongo_customer['states'])
            print(f'\nObjectId {obj_id}\nFirst Name: {first_name}\n'
                  f'Last Name: {last_name}\nCompany Name: {company_name}\nPhone: {phone}\n'
                  f'Address: {adress1}\nAddress 2: {adress2}\nCity: {city}\nZip Code: {zip_code}\nCountry: {country}\n'
                  f'Sales Representant: {sales_representant}\nState: {states}')
            print("*" * 70)


def insert_one_customer():
    first_name = str(input("First Name: "))
    last_name = str(input("Last name: "))
    company_name = input("Company Name: ")
    phone = str(input("Phone: "))
    adress1 = str(input("Adress: "))
    adress2 = str(input("Adress2: "))
    city = str(input("City: "))
    zip_code = str(input("Zip Code: "))
    country = str(input("Country: "))
    sales_representant = str(input("Sales Representant: "))
    states = str(input("State: "))
    reg_no = str(input("Reg No: "))
    manufacturer = str(input("Manufacturer: "))
    color = str(input("Color: "))
    model = str(input("Model: "))
    year_model = str(input("Year Model: "))
    owner_id = str(input("Owner ID: "))
    payment_date = str(input("Payment date: "))
    payment_amount = str(input("Payment Amount: "))
    customer_paid_bill_id = str(input("Customer Paid bill id: "))
    staffs_id_staff = str(input("Staffs id: "))
    customers_id_customers = str(input("Customer ID: "))

    super_customer_key_list_mongo = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                                     'city', 'zip_code', 'country', 'sales_representant', 'states', 'reg_no',
                                     'manufacturer',
                                     'color', 'model', 'year_model', 'owner_id', 'payment_date', 'payment_amount',
                                     'customer_paid_bill_id', 'staffs_id_staff', 'customers_id_customers']

    create_single_customer = [first_name, last_name, company_name,
                              phone,
                              adress1,
                              adress2, city, zip_code,
                              country, sales_representant, states,
                              reg_no, manufacturer, color,
                              model,
                              year_model, owner_id, payment_date,
                              payment_amount, customer_paid_bill_id,
                              staffs_id_staff, customers_id_customers]

    single_customer = dict(zip(super_customer_key_list_mongo, create_single_customer))

    db.customers.insert_one(single_customer)
    print("Added one Mongo customer successfully")


def delete_one_mongo_customer(xxx):
    id_finder2 = db.customers.find({"_id": ObjectId(xxx)})
    num_cars = 0
    num_payments = 0
    num_staff = 0
    # delete_car(xxx)
    for mongo_customer in id_finder2:
        obj_id = (mongo_customer['_id'])
        first_name = (mongo_customer['first_name'])  # ['_id'])
        last_name = (mongo_customer['last_name'])
        company_name = (mongo_customer['company_name'])
        phone = (mongo_customer['phone'])
        adress1 = (mongo_customer['adress1'])
        adress2 = (mongo_customer['adress2'])
        city = (mongo_customer['city'])
        zip_code = (mongo_customer['zip_code'])
        country = (mongo_customer['country'])
        sales_representant = (mongo_customer['sales_representant'])
        states = (mongo_customer['states'])

    # Here we start searching for the number of cars this person has.
    id_finder3 = db.customers.find(({"owner_id": ObjectId(xxx)}))
    records3 = list(id_finder3)
    if len(records3) == 0:
        print("This customer dont have any cars.")
        reg_no = ""
        manufacturer = ""
        color = ""
        model = ""
        year_model = ""
        owner_id = ""

    else:

        # Create a number of cars list the person has.
        collected_cars_list = []
        for m1 in records3:
            reg_no = (m1['reg_no'])
            manufacturer = (m1['manufacturer'])
            color = (m1['color'])
            model = (m1['model'])
            year_model = (m1['year_model'])
            owner_id = (m1['owner_id'])
            collected_cars_list.append(reg_no)
        num_cars = len(collected_cars_list)

        # Here we start searching for customer paid_bills_id connection.
    id_finder4 = db.customers.find(({"customer_paid_bill_id": ObjectId(xxx)}))
    records4 = list(id_finder4)
    if len(records4) == 0:
        print("This customer dont have any payments")
        payments_no = ""
        payment_date = ""
        payment_amount = ""
        customer_paid_bill_id = ""
    else:
        collected_paid_bills_id = []
        for m2 in records4:
            payments_no = (m2['payments_no'])
            payment_date = (m2['payment_date'])
            payment_amount = (m2['payment_amount'])
            customer_paid_bill_id = (m2['customer_paid_bill_id'])
            collected_paid_bills_id.append(payments_no)
        num_payments = len(collected_paid_bills_id)

    # Here we start to search for which staff has customers
    id_finder5 = db.customers.find(({"customers_id_customers": ObjectId(xxx)}))
    records5 = list(id_finder5)
    if len(records5) == 0:
        print("this customer doesnt have any staff.")
        staffs_id_staff = ""
        customers_id_customers = ""
    else:
        our_sales_personal = []
        for m3 in records5:
            staffs_id_staff = (m3['staffs_id_staff'])
            customers_id_customers = (m3['customers_id_customers'])
            our_sales_personal.append(staffs_id_staff)
        num_staff = len(our_sales_personal)

    # View the customer before you decide if you want to delete him/her.
    print(f'\nObjectId {obj_id}\nFirst Name: {first_name}\n'
          f'Last Name: {last_name}\nCompany Name: {company_name}\nPhone: {phone}\n'
          f'Address: {adress1}\nAddress 2: {adress2}\nCity: {city}\nZip Code: {zip_code}\nCountry: {country}\n'
          f'Sales Representant: {sales_representant}\nState: {states}\n'
          f'reg no: {reg_no}\n:manufacturer {manufacturer}\n'
          f'color: {color}\nModel: {model}\nyear model: {year_model}\nowner id: {owner_id}\npayments no: {payments_no}\n'
          f'payment date: {payment_date}\npayment amount: {payment_amount}\n'
          f'customer paid bill id: {customer_paid_bill_id}'
          f'staff id staff: {staffs_id_staff}\ncustomers id customers: {customers_id_customers}')

    print()
    print()
    to_delete_or_not_delete_is_the_question = str(input("Do you want to delete this customer ? (yes/no)\n< "))
    if to_delete_or_not_delete_is_the_question[0] == "y":

        # This block deletes customer
        db.customers.update({'_id': obj_id}, {'$unset': {'first_name': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'last_name': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'company_name': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'phone': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'adress1': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'adress2': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'city': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'zip_code': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'country': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'sales_representant': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'states': ""}})

        # This block deletes cars
        # Here we need to initiate a loop so we can take away all cars the customer has.
        for delete_som_cars in range(0, num_cars):
            delete_car(xxx)

        # This block deletes payments
        # Here we need to initiate a loop so we can take away all customer paid bills.
        for delete_some_paid_bills in range(0, num_payments):
            delete_payments(xxx)

        # This block deletes staff has customers
        # Here we need to make an loop to take away all the staffs customer contacts.
        for delete_som_staff_contacts in range(0, num_staff):
            delete_staff_has_customers(xxx)

        print(f"Deleted customer and the document with object id: {obj_id}")
        print()
    else:
        # Jump back to the menu.
        pass


def delete_car(xxx):
    items = db.customers.find(({"owner_id": ObjectId(xxx)}))
    for m1 in items:
        reg_no = (m1['reg_no'])
        manufacturer = (m1['manufacturer'])
        color = (m1['color'])
        model = (m1['model'])
        year_model = (m1['year_model'])
        owner_id = (m1['owner_id'])
        obj_id = (m1['_id'])  # "61b90d140d053fd1561a9275"
        db.customers.update({'_id': obj_id}, {'$unset': {'reg_no': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'manufacturer': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'color': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'model': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'year_model': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'owner_id': ""}})


def delete_payments(xxx):
    id_finder4 = db.customers.find(({"customer_paid_bill_id": ObjectId(xxx)}))
    for m2 in id_finder4:
        payments_no = (m2['payments_no'])
        payment_date = (m2['payment_date'])
        payment_amount = (m2['payment_amount'])
        customer_paid_bill_id = (m2['customer_paid_bill_id'])
        obj_id = (m2['_id'])
        db.customers.update({'_id': obj_id}, {'$unset': {'payments_no': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'payment_date': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'payment_amount': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'customer_paid_bill_id': ""}})


def delete_staff_has_customers(xxx):
    id_finder5 = db.customers.find(({"customers_id_customers": ObjectId(xxx)}))
    for m3 in id_finder5:
        staffs_id_staff = (m3['staffs_id_staff'])
        customers_id_customers = (m3['customers_id_customers'])
        obj_id = (m3['_id'])

        db.customers.update({'_id': obj_id}, {'$unset': {'staffs_id_staff': ""}})
        db.customers.update({'_id': obj_id}, {'$unset': {'customers_id_customers': ""}})


def update_mongo_customer(xxx):
    running = True

    while running:
        update_finder = db.customers.find({"_id": ObjectId(xxx)})
        if update_finder is None:
            print("Cannot update, the person doesnt exist.")
            main()

        else:

            for mongo_customer in update_finder:
                obj_id = (mongo_customer['_id'])
                first_name = (mongo_customer['first_name'])  # ['_id'])
                last_name = (mongo_customer['last_name'])
                company_name = (mongo_customer['company_name'])
                phone = (mongo_customer['phone'])
                adress1 = (mongo_customer['adress1'])
                adress2 = (mongo_customer['adress2'])
                city = (mongo_customer['city'])
                zip_code = (mongo_customer['zip_code'])
                country = (mongo_customer['country'])
                sales_representant = (mongo_customer['sales_representant'])
                states = (mongo_customer['states'])

            print(f'\nObjectId {obj_id}\nFirst Name: {first_name}\n'
                  f'Last Name: {last_name}\nCompany Name: {company_name}\nPhone: {phone}\n'
                  f'Address: {adress1}\nAddress 2: {adress2}\nCity: {city}\nZip Code: {zip_code}\nCountry: {country}\n'
                  f'Sales Representant: {sales_representant}\nState: {states}\n')

            print()
            print('*******************************************************************')

            print("Press (1) for update first name")
            print("Press (2) for update last name")
            print("Press (3) for update company name")
            print("Press (4) for update phone")
            print("Press (5) for update adress 1")
            print("Press (6) for update adress 2")
            print("Press (7) for update city")
            print("Press (8) for update zip code")
            print("Press (9) for update country")
            print("Press (10) for update sales_representant")
            print("Press (11) for update state")
            valet = str(input('Press number to update: '))

            if valet == "1":
                choice = str(input('Enter a new first name: '))
                db.customers.update({'_id': obj_id}, {'$set': {'first_name': choice}})

                print("Updated first name field")

            elif valet == "2":
                choice = str(input('Enter a new last name: '))
                db.customers.update({'_id': obj_id}, {'$set': {'last_name': choice}})
                print("Updated last name field")

            elif valet == "3":
                choice = str(input('Enter a new company name: '))
                db.customers.update({'_id': obj_id}, {'$set': {'company_name': choice}})
                print("Updated company field.")

            elif valet == "4":
                choice = str(input('Enter a new phone: '))
                db.customers.update({'_id': obj_id}, {'$set': {'phone': choice}})
                print("Updated phone field.")

            elif valet == "5":
                choice = str(input('Enter a new address: '))
                db.customers.update({'_id': obj_id}, {'$set': {'adress1': choice}})
                print("Updated adress 1 field.")

            elif valet == "6":
                choice = str(input('Enter a new adress 2: '))
                db.customers.update({'_id': obj_id}, {'$set': {'adress2': choice}})
                print("Updated adress 2 field.")

            elif valet == "7":
                choice = str(input('Enter a new city: '))
                db.customers.update({'_id': obj_id}, {'$set': {'city': choice}})
                print("Updated city field.")

            elif valet == "8":
                choice = str(input('Enter a new zip code: '))
                db.customers.update({'_id': obj_id}, {'$set': {'zip_code': choice}})
                print("Updated zip code field.")

            elif valet == "9":
                choice = str(input('Enter a new country: '))
                db.customers.update({'_id': obj_id}, {'$set': {'country': choice}})
                print("Updated country field")

            elif valet == "10":
                choice = str(input('Enter a new sales representant: '))
                db.customers.update({'_id': obj_id}, {'$set': {'sales_representant': choice}})
                print("Updated sales representant field")

            elif valet == "11":
                choice = str(input('Enter a new state: '))
                db.customers.update({'_id': obj_id}, {'$set': {'states': choice}})
                print("Updated state field")

            update_finder = db.customers.find({"_id": ObjectId(xxx)})

            for mongo_customer in update_finder:
                obj_id = (mongo_customer['_id'])
                first_name = (mongo_customer['first_name'])  # ['_id'])
                last_name = (mongo_customer['last_name'])
                company_name = (mongo_customer['company_name'])
                phone = (mongo_customer['phone'])
                adress1 = (mongo_customer['adress1'])
                adress2 = (mongo_customer['adress2'])
                city = (mongo_customer['city'])
                zip_code = (mongo_customer['zip_code'])
                country = (mongo_customer['country'])
                sales_representant = (mongo_customer['sales_representant'])
                states = (mongo_customer['states'])

            print(f'\nObjectId {obj_id}\nFirst Name: {first_name}\n'
                  f'Last Name: {last_name}\nCompany Name: {company_name}\nPhone: {phone}\n'
                  f'Address: {adress1}\nAddress 2: {adress2}\nCity: {city}\nZip Code: {zip_code}\nCountry: {country}\n'
                  f'Sales Representant: {sales_representant}\nState: {states}\n')
            print()

            sista_valet = str(input('Are you finished updating? (yes/no)? '))
            if sista_valet[0] == "y":
                running = False

                # mongo_menu()
                main()
            else:
                continue
