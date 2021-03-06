DROP TABLE transactions;
DROP TABLE categories;
DROP TABLE merchants;

CREATE TABLE merchants (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  activated BOOLEAN
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  activated BOOLEAN
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  transaction_date date,
  merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
  category_id INT REFERENCES categories(id) ON DELETE SET NULL,
  amount INT
);
