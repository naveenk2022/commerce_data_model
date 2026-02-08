from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Identity,
    Text,
    DateTime,
    Table,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, Identity(always=True), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)

    orders = relationship(
        "Order",
        back_populates="customer",
        cascade="all, delete-orphan",
    )


class OrderProduct(Base):
    __tablename__ = "order_products"
    order_id = Column(
        Integer,
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        primary_key=True,
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id", ondelete="CASCADE"),
        primary_key=True,
    )

    product_count = Column(Integer, server_default="1", nullable=False)
    order = relationship("Order", back_populates="products")
    product = relationship("Product", back_populates="orders")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, Identity(always=True), primary_key=True)
    customer_id = Column(
        Integer, ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False
    )
    order_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    customer = relationship(
        "Customer",
        back_populates="orders",
    )
    products = relationship(
        "OrderProduct",
        back_populates="order",
        cascade="all, delete-orphan",
    )


product_tags = Table(
    "product_tags",
    Base.metadata,
    Column(
        "product_id",
        ForeignKey("products.product_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("tag_id", ForeignKey("tags.tag_id", ondelete="CASCADE"), primary_key=True),
)


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, Identity(always=True), primary_key=True)
    product_name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    last_edited = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    orders = relationship(
        "OrderProduct",
        back_populates="product",
        cascade="all, delete-orphan",
    )
    tags = relationship("Tag", secondary=product_tags, back_populates="products")


class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, Identity(always=True), primary_key=True)
    name = Column(String, nullable=False, unique=True)
    products = relationship("Product", secondary=product_tags, back_populates="tags")
