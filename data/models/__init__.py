from sqlalchemy import Integer, Column, String, ForeignKey, Date, Text, DECIMAL, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB
from sqlalchemy.orm import relationship

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
    customer_cars_reg_no = Column(String(20), ForeignKey('customer_cars_reg_no'))
    orders_order_no = Column(Integer, ForeignKey('orders_order_no'))

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
   # cps_orders = relationship('CpsOrder')


class ManufacturerHasCpsOrder(Base):
    __tablename__ = "manufacturers_has_cps_orders"
    __table_args__ = (
        PrimaryKeyConstraint('manufacturers_manufacturer_id', 'cps_orders_internal_order_no'),
    )
    manufacturers_manufacturer_id = Column(Integer, ForeignKey('manufacturers_manufacturer_id'))
    cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders_internal_order_no'))

    Manufacture = relationship('manufacturers')
    CpsOrder = relationship('cps_orders')


class Order(Base):
    __tablename__ = "orders"

    order_no = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date, nullable=False)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)


class CpsOrder(Base):
    __tablename__ = "cps_orders"

    internal_order_no = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    required_date = Column(Date)
    shipping_date = Column(Date)
    status = Column(String(45), nullable=False)
    comments = Column(Text)
    order_no_comments = Column(Text)


class CustomerCar(Base):
    __tablename__ = "customer_cars"

    reg_no = Column(String(20), primary_key=True, nullable=False)
    manufacturer = Column(String(100), nullable=False)
    color = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year_model = Column(String(45), nullable=False)
    customer_cars = relationship('CustomerCar')
    # customer_cars = relationship("Customer", back_populates="customer_cars")


class OrderDetail(Base):
    __tablename__ = "ordersdetails"
    __table_args__ = (
        PrimaryKeyConstraint('orders_order_no', 'products_product_id'),
    )

    orders_order_no = Column(Integer, ForeignKey('orders_order_no'))
    products_product_id = Column(Integer, ForeignKey('products_product_id'))
    quantity = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(10, 2), nullable=False)
    Order = relationship('orders')
    Product = relationship('products')


class Payment(Base):
    __tablename__ = "payments"

    payments_no = Column(Integer, primary_key=True, autoincrement=True)
    payment_date = Column(Date, nullable=False)
    payment_amount = Column(DECIMAL(10, 2), nullable=False)
    customers_id_customers = Column(Integer, ForeignKey('customers.id_customers'))
    Customer = relationship('customers')


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
    Productline = relationship('productlines')


class Staff(Base):
    __tablename__ = "staffs"

    id_staff = Column(Integer, primary_key=True, autoincrement=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    job_title = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    reports_to = Column(String(45))
    store = Column(String(45))


class StaffHasCpsOrder(Base):
    __tablename__ = "staffs_has_cpsorders"
    __table_args__ = (
        PrimaryKeyConstraint('staffs_id_staff', 'cps_orders_internal_order_no'),
    )
    staffs_id_staff = Column(Integer, ForeignKey('staffs_id_staff'))
    cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders_internal_order_no'))
    Staff = relationship('staffs')
    CpsOrder = relationship('cps_orders')


class StaffHasCustomer(Base):
    __tablename__ = "staffs_has_customers"
    __table_args__ = (
        PrimaryKeyConstraint('staffs_id_staff', 'customers_id_customers'),
    )
    staffs_id_staff = Column(Integer, ForeignKey('staffs_id_staff'))
    customers_id_customers = Column(Integer, ForeignKey('customers_id_customers'))
    Staff = relationship('staffs')
    Customer = relationship('customers')


class StaffHasStaff(Base):
    __tablename__ = "staffs_has_staffs"
    __table_args__ = (
        PrimaryKeyConstraint('staffs_id_staff', 'staffs_id_staff1'),
    )
    staffs_id_staff = Column(Integer, ForeignKey('staffs_id_staff'))
    staffs_id_staff1 = Column(Integer, ForeignKey('staffs_id_staff1'))
    Staff = relationship('staffs')


class Storage(Base):
    __tablename__ = "storage"

    storage_id = Column(Integer, primary_key=True, autoincrement=True)
    storage_name = Column(String(150), nullable=False)
    storage_quantity = Column(Integer, nullable=False)
    storage_city = Column(String(100), nullable=False)


class StorageHasProducts(Base):
    __tablename__ = "storage_has_products"
    __table_args__ = (
        PrimaryKeyConstraint('storage_storage_id', 'products_product_id'),
    )
    storage_storage_id = Column(Integer, ForeignKey('storage_storage_id'))
    products_product_id = Column(Integer, ForeignKey('products_product_id'))
    Storage = relationship('storage')
    Product = relationship('products')


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


class SupplierHasCpsOrder(Base):
    __tablename__ = "suppliers_has_cps_orders"
    __table_args__ = (
        PrimaryKeyConstraint('suppliers_supplier_id', 'cps_orders_internal_order_no'),
    )
    suppliers_supplier_id = Column(Integer, ForeignKey('suppliers_supplier_id'))
    cps_orders_internal_order_no = Column(Integer, ForeignKey('cps_orders_internal_order_no'))
    Supplier = relationship('suppliers')
    CpsOrder = relationship('cps_orders')
