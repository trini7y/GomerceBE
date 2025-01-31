from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .admin import Admin
from .coupon import Coupon
from .customer import Customer
from .order_detail import OrderDetail
from .order import Order
from .payment_detail import PaymentDetail
from .payment_method import PaymentMethod
from .product_category import ProductCategory
from .product import Product
from .review import Review
from .seller import Seller
from .shipping_address import ShippingAddress
from .status import Status
from .store import Store
from .verification_token import VerificationToken