from sqlalchemy import Integer, Column, String, ForeignKey, Date, Text, DECIMAL
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB

from data.db import Base


class Customer(Base):
    __tablename__ = "customers"

    id_customers = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    company_name = Column(String(100))
    phone = Column(String(45), nullable=False)
    address1 = Column(String(150), nullable=False)
    address2 = Column(String(150))
    city = Column(String(100), nullable=False)
    zip_code = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    sales_representant = Column(String(150), nullable=False)
    states = Column(String(100))
    customer_cars_reg_no = Column(String(20), ForeignKey('customer_cars.reg_no'))
    orders_order_no = Column(Integer, ForeignKey('orders.order_no'))


class Manufacture(Base):
    __tablename__ = "manufactures"

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    name_manufacturer = Column(String(45), nullable=False)
    main_office_adress1 = Column(String(100), nullable=False)
    main_office_adress2 = Column(String(100))
    main_office_name = Column(String(100), nullable=False)
    contact_person_name = Column(String(200), nullable=False)
    contact_person_phone = Column(String(45), nullable=False)
    contact_person_email = Column(String(45), nullable=False)


class ManufacturerHasCpsOrder(Base):
    __tablename__ = "manufactures_has_cps_orders"

    manufacturers_manufacturer_id = Column(Integer, ForeignKey('manufacturers.manufacturer_id'))
    cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders.internal_order_no'))


class Order(Base):
    __tablename__ = "orders"
    order_no = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date,  nullable=False)
    required_date = Column(Date, nullable=False)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)


class CpsOrder(Base):
    __tablename__ = "cps_orders"
    internal_order_no = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)
    order_no_comments = Column(Text)


class CustomerCar(Base):
    __tablename__ = "customers_cars"
    reg_no = Column(String(20), primary_key=True, nullable=False)
    manufacturer = Column(String(100), nullable=False)
    color = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(String(45), nullable=False)


class OrderDetail(Base):
    __tablename__ = "ordersdetails"
    orders_order_no = Column(Integer, ForeignKey('orders.order_no'))
    products_product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(10, 2), nullable=False)


class Payment(Base):
    __tablename__ = "payments"
    payments_no = Column(Integer, primary_key=True, autoincrement=True)
    # payment_date = Column(String(45), nullable=False)
    payment_amount = Column(DECIMAL(10, 2), nullable=False)
    customers_id_customers = Column(Integer, ForeignKey('customers.id_customers'))


class Productline(Base):
    __tablename__ = "productlines"
    productline = Column(String(50), primary_key=True, nullable=False)
    text_description = Column(String(5000))
    html_description = Column(MEDIUMTEXT)
    image = Column(MEDIUMBLOB)
