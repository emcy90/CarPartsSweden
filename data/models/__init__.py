from sqlalchemy import Integer, Column, String, ForeignKey

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

