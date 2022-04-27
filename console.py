from models.category import Category
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.category_repository as category_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

category_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

category1 = Category('Groceries')
category_repository.save(category1)

merchant1 = Category('Tesco')
merchant_repository.save(merchant1)

transaction1 = Transaction('2022-04-27', merchant1, 999, category1)
transaction_repository.save(transaction1)

transaction2 = Transaction('2022-04-27', merchant1, 500, category1)
transaction_repository.save(transaction2)

breakpoint()