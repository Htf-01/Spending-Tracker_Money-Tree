DROP TABLE transactions;
DROP TABLE categories;
DROP TABLE merchants;

CREATE TABLE merchants (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  activated BOOLEAN,
  filtered BOOLEAN
);
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  activated BOOLEAN,
  filtered BOOLEAN
);

CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
  category_id INT REFERENCES categories(id) ON DELETE set null,
  amount INT
);