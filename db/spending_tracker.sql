DROP TABLE transactions;
DROP TABLE categories;
DROP TABLE merchants;
DROP TABLE budgets;

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
CREATE TABLE budgets (
  id SERIAL PRIMARY KEY,
  budget_date date
);
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  transaction_date date,
  merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
  category_id INT REFERENCES categories(id) ON DELETE SET NULL,
  amount INT,
  budget_id INT REFERENCES budgets(id) ON DELETE SET NULL
);



Insert into budgets (budget_date) values ('2020-01-01');
Insert into budgets (budget_date) values ('2020-02-01');
Insert into budgets (budget_date) values ('2020-03-01');
Insert into budgets (budget_date) values ('2020-04-01');
Insert into budgets (budget_date) values ('2020-05-01');
Insert into budgets (budget_date) values ('2020-06-01');
Insert into budgets (budget_date) values ('2020-07-01');
Insert into budgets (budget_date) values ('2020-08-01');
Insert into budgets (budget_date) values ('2020-09-01');
Insert into budgets (budget_date) values ('2020-10-01');
Insert into budgets (budget_date) values ('2020-11-01');
Insert into budgets (budget_date) values ('2020-12-01');
Insert into budgets (budget_date) values ('2021-01-01');
Insert into budgets (budget_date) values ('2021-02-01');
Insert into budgets (budget_date) values ('2021-03-01');
Insert into budgets (budget_date) values ('2021-04-01');
Insert into budgets (budget_date) values ('2021-05-01');
Insert into budgets (budget_date) values ('2021-06-01');
Insert into budgets (budget_date) values ('2021-07-01');
Insert into budgets (budget_date) values ('2021-08-01');
Insert into budgets (budget_date) values ('2021-09-01');
Insert into budgets (budget_date) values ('2021-10-01');
Insert into budgets (budget_date) values ('2021-11-01');
Insert into budgets (budget_date) values ('2021-12-01');
Insert into budgets (budget_date) values ('2022-01-01');
Insert into budgets (budget_date) values ('2022-02-01');
Insert into budgets (budget_date) values ('2022-03-01');
Insert into budgets (budget_date) values ('2022-04-01');
Insert into budgets (budget_date) values ('2022-05-01');
Insert into budgets (budget_date) values ('2022-06-01');
Insert into budgets (budget_date) values ('2022-07-01');
Insert into budgets (budget_date) values ('2022-08-01');
Insert into budgets (budget_date) values ('2022-09-01');
Insert into budgets (budget_date) values ('2022-10-01');
Insert into budgets (budget_date) values ('2022-11-01');
Insert into budgets (budget_date) values ('2022-12-01');
Insert into budgets (budget_date) values ('2023-01-01');
Insert into budgets (budget_date) values ('2023-02-01');
Insert into budgets (budget_date) values ('2023-03-01');
Insert into budgets (budget_date) values ('2023-04-01');
Insert into budgets (budget_date) values ('2023-05-01');
Insert into budgets (budget_date) values ('2023-06-01');
Insert into budgets (budget_date) values ('2023-07-01');
Insert into budgets (budget_date) values ('2023-08-01');
Insert into budgets (budget_date) values ('2023-09-01');
Insert into budgets (budget_date) values ('2023-10-01');
Insert into budgets (budget_date) values ('2023-11-01');
Insert into budgets (budget_date) values ('2023-12-01');
Insert into budgets (budget_date) values ('2024-01-01');
Insert into budgets (budget_date) values ('2024-02-01');
Insert into budgets (budget_date) values ('2024-03-01');
Insert into budgets (budget_date) values ('2024-04-01');
Insert into budgets (budget_date) values ('2024-05-01');
Insert into budgets (budget_date) values ('2024-06-01');
Insert into budgets (budget_date) values ('2024-07-01');
Insert into budgets (budget_date) values ('2024-08-01');
Insert into budgets (budget_date) values ('2024-09-01');
Insert into budgets (budget_date) values ('2024-10-01');
Insert into budgets (budget_date) values ('2024-11-01');
Insert into budgets (budget_date) values ('2024-12-01');