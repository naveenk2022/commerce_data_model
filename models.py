from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Identity,
    Text,
    DateTime,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id = Column(
        Integer, Identity(always=True), primary_key=True
    )
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    
    orders = relationship(
        "Order",
        back_populates="customer",
        cascade="all, delete-orphan",
    )

class Order(Base):
    __tablename__ = "orders"
    
    order_id = Column(
        Integer, Identity(always=True), primary_key=True
    )
    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id", ondelete="CASCADE"),
        nullable=False
    )
    order_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    
    customer = relationship(
        "Customer", 
        back_populates="orders"
    )

class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(
        Integer, Identity(always=True), primary_key=True
    )
    product_name = Column(
        String, nullable=False
    )
    description = Column(Text)
    price = Column(Float, nullable=False)


