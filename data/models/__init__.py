from sqlalchemy import Integer, Column, String, ForeignKey, Date, Text, DECIMAL, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
from sqlalchemy.orm import relationship

from data.db import Base


class StaffHasCustomer(Base):
    __tablename__ = "staffs_has_customers"

    staffs_id_staff = Column(Integer, ForeignKey('staffs.id_staff'), primary_key=True)
    customers_id_customers = Column(Integer, ForeignKey('customers.id_customers'), primary_key=True)
    children = relationship('Staff', back_populates='parents')
    child = relationship('Customer', back_populates='parents')


class ManufacturerHasCpsOrder(Base):
    __tablename__ = "manufacturers_has_cps_orders"

    manufacturers_manufacturer_id = Column(ForeignKey('manufacturers.manufacturer_id'), primary_key=True)
    cps_orders_internal_order_no = Column(ForeignKey('cps_orders.internal_order_no'), primary_key=True)
    parent = relationship('Manufacture', back_populates='children')
    child = relationship('CpsOrder', back_populates='parents')


class StaffHasCpsOrder(Base):
    __tablename__ = "staffs_has_cpsorders"
    # __table_args__ = (
    #     PrimaryKeyConstraint('staffs_id_staff', 'cps_orders_internal_order_no'),
    # )
    staffs_id_staff = Column(Integer, ForeignKey('staffs.id_staff'), primary_key=True)
    cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders.internal_order_no'), primary_key=True)
    staffs = relationship('Staff')
    cps_orders = relationship('CpsOrder')


class StaffHasStaff(Base):
    __tablename__ = "staffs_has_staffs"

    staffs_id_staff = Column(Integer, ForeignKey('staffs.id_staff'), primary_key=True)
    staffs_id_staff1 = Column(Integer, ForeignKey('staffs.id_staff'), primary_key=True)
    barn1 = relationship('Staff', back_populates='mamma1', foreign_keys=[staffs_id_staff1])
    barn = relationship('Staff', back_populates='mamma', foreign_keys=[staffs_id_staff])
    # staffs = relationship('Staff', back_populates='staffs')
    # children = relationship('Staff')


class OrderDetail(Base):
    __tablename__ = "ordersdetails"

    orders_order_no = Column(Integer, ForeignKey('orders.order_no'), primary_key=True)
    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(10, 2), nullable=False)
    product = relationship('Product', back_populates="product_to_order")
    order = relationship('Order', back_populates="order_to_product")


class StorageHasProducts(Base):
    __tablename__ = "storage_has_products"
    # __table_args__ = (
    #     PrimaryKeyConstraint('storage_storage_id', 'products_product_id'),
    # )
    storage_storage_id = Column(Integer, ForeignKey('storage.storage_id'), primary_key=True)
    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    storage = relationship('Storage')
    products = relationship('Product')


# class SupplierHasCpsOrder(Base):
#     __tablename__ = "suppliers_has_cps_orders"
#     # __table_args__ = (
#     #     PrimaryKeyConstraint('suppliers_supplier_id', 'cps_orders_internal_order_no'),
#     # )
#     suppliers_supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
#     cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders.internal_order_no'), primary_key=True)
#     suppliers = relationship('Supplier')
#     cps_orders = relationship('cps_orders')

class Customer(Base):
    __tablename__ = "customers"

    id_customers = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    company_name = Column(String(100))
    phone = Column(String(45), nullable=False)
    adress1 = Column(String(150), nullable=False)
    adress2 = Column(String(150))
    city = Column(String(100), nullable=False)
    zip_code = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    sales_representant = Column(String(150), nullable=False)
    states = Column(String(100))
    customer_cars = relationship('CustomerCar', back_populates="owner")
    payments = relationship('Payment', back_populates="customer_paid_bill")
    parents = relationship('StaffHasCustomer', back_populates='child')

    # customers_id_customers = Column(Integer, ForeignKey('customers.id_customers'))
    # customer_cars_reg_no = Column(String(20), ForeignKey('customer.cars_reg_no'))
    # CustomerCar = relationship("customer_cars", back_populates="customer")
    # orders = relationship('Order')



class Manufacture(Base):
    __tablename__ = "manufacturers"

    manufacturer_id = Column(Integer, primary_key=True, autoincrement=True)
    name_manufacturer = Column(String(45), nullable=False)
    main_office_adress1 = Column(String(100), nullable=False)
    main_office_adress2 = Column(String(100))
    main_office_name = Column(String(100), nullable=False)
    contact_person_name = Column(String(200), nullable=False)
    contact_person_phone = Column(String(45), nullable=False)
    contact_person_email = Column(String(45), nullable=False)
    # manufacturers_has_cps_orders = Column(Integer, ForeignKey('manufacturers_has_cps_orders.manufacturers_manufacturer_id'))
    children = relationship('ManufacturerHasCpsOrder', back_populates='parent')
    # cps_orders = relationship('CpsOrder')
    # manufacturers = relationship('Manufacture')


class Order(Base):
    __tablename__ = "orders"

    order_no = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date, nullable=False)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)
    customers_id_customers = Column(Integer, ForeignKey('customers.id_customers'))
    order_to_product = relationship('OrderDetail', back_populates="order")


class CpsOrder(Base):
    __tablename__ = "cps_orders"

    internal_order_no = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)
    order_no_comments = Column(Text)
    parents = relationship('ManufacturerHasCpsOrder', back_populates='child')
    # manufacturers = relationship('Manufacture')


class CustomerCar(Base):
    __tablename__ = "customer_cars"

    reg_no = Column(String(20), primary_key=True, nullable=False)
    manufacturer = Column(String(100), nullable=False)
    color = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(String(45), nullable=False)
    owner_id = Column(Integer, ForeignKey('customers.id_customers'))
    owner = relationship('Customer', back_populates="customer_cars")
    # customer_cars = relationship("Customer", back_populates="customer_cars")


class OrderDetail(Base):
    __tablename__ = "ordersdetails"

    orders_order_no = Column(Integer, ForeignKey('orders.order_no'), primary_key=True)
    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(10, 2), nullable=False)
    product = relationship('Product', back_populates="product_to_order")
    order = relationship('Order', back_populates="order_to_product")


class Payment(Base):
    __tablename__ = "payments"

    payments_no = Column(Integer, primary_key=True, autoincrement=True)
    payment_date = Column(Date, nullable=False)
    payment_amount = Column(DECIMAL(10, 2), nullable=False)
    customer_paid_bill_id = Column(Integer, ForeignKey('customers.id_customers'))
    customer_paid_bill = relationship('Customer', back_populates="payments")


class Productline(Base):
    __tablename__ = "productlines"

    productline = Column(String(50), primary_key=True, nullable=False)
    text_description = Column(String(5000))
    html_description = Column(MEDIUMTEXT)
    image = Column(MEDIUMBLOB)


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(45), nullable=False)
    product_description = Column(Text, nullable=False)
    inprice = Column(DECIMAL(10, 2), nullable=False)
    outprice = Column(DECIMAL(10, 2), nullable=False)
    productlines = Column(String(50), ForeignKey('productlines.productline'))
    product_to_order = relationship('OrderDetail', back_populates="product")


class Staff(Base):
    __tablename__ = "staffs"

    id_staff = Column(Integer, primary_key=True, autoincrement=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    job_title = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    reports_to = Column(String(45))
    store = Column(String(45))
    parents = relationship('StaffHasCustomer', back_populates='children')
    mamma = relationship('StaffHasStaff', back_populates='barn')
    mamma1 = relationship('StaffHasStaff', back_populates='barn1')
    # children = relationship('StaffHasCustomer', back_populates='parent')


class Storage(Base):
    __tablename__ = "storage"

    storage_id = Column(Integer, primary_key=True, autoincrement=True)
    storage_name = Column(String(150), nullable=False)
    storage_quantity = Column(Integer, nullable=False)
    storage_city = Column(String(100), nullable=False)


class StorageHasProducts(Base):
    __tablename__ = "storage_has_products"
    # __table_args__ = (
    #     PrimaryKeyConstraint('storage_storage_id', 'products_product_id'),
    # )
    storage_storage_id = Column(Integer, ForeignKey('storage.storage_id'), primary_key=True)
    products_product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    storage = relationship('Storage')
    products = relationship('Product')


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(45), nullable=False)
    supplier_address1 = Column(String(45), nullable=False)
    supplier_address2 = Column(String(45))
    city = Column(String(100), nullable=False)
    zip_code = Column(String(45), nullable=False)
    country = Column(String(45), nullable=False)
    contact_person = Column(String(100))
    phone_number = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

# class SupplierHasCpsOrder(Base):
#     __tablename__ = "suppliers_has_cps_orders"
#     # __table_args__ = (
#     #     PrimaryKeyConstraint('suppliers_supplier_id', 'cps_orders_internal_order_no'),
#     # )
#     suppliers_supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'), primary_key=True)
#     cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders.internal_order_no'), primary_key=True)
#     suppliers = relationship('Supplier')
#     cps_orders = relationship('cps_orders')
