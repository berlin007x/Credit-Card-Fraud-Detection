# 💳 Credit Card Fraud Detection using SQL

An SQL project for analyzing credit card transactions and detecting fraud using **PostgreSQL**. This project explores customer profiles, transaction behaviors, and fraud patterns through various SQL queries.

---

## 📌 Objective

To identify fraudulent transactions and uncover trends by analyzing:
- Customer details
- Credit card information
- Transaction behavior
- Fraud detection flags

---

## 🛠️ Technologies Used

- **PostgreSQL** for database management
- **SQL** for data analysis (Joins, Aggregations, Grouping, Filters)
- **pgAdmin** for running queries
- **CSV Files** for importing data
- **Git & GitHub** for version control

---

## 📂 Project Files

- **`dataset/`**: Contains the CSV files:
  - `card_base.csv` - Credit card data
  - `customer_base.csv` - Customer information
  - `transaction_base.csv` - Transaction records
  - `fraud_base.csv` - Fraud flag data
  
- **`create_tables.sql`**: Script for creating PostgreSQL tables from the CSV files.
- **`fraud_analysis_queries.sql`**: Contains SQL queries to analyze fraud patterns.

---

## 🔍 Key Queries

1. **Customers with transactions over 49000**
2. **Premium credit card eligibility based on customer type**
3. **Credit limit range for fraudulent transaction customers**
4. **Average age of fraud-affected customers based on card type**
5. **Month with the highest number of fraudulent transactions**
6. **Customer with the highest non-fraudulent transaction value**

---

## 🚀 How to Use

1. **Set up PostgreSQL**: Install from [PostgreSQL Downloads](https://www.postgresql.org/download/) or use a cloud service like [ElephantSQL](https://www.elephantsql.com/).
2. **Create the Database**: Use **pgAdmin** or **DBeaver** to create a new PostgreSQL database.
3. **Import Data**: Load the CSV files into the corresponding tables.
4. **Run SQL Scripts**: Execute `create_tables.sql` to set up your tables, and then run `fraud_analysis_queries.sql` to analyze the data.

---

## 💡 Conclusion

This project utilizes SQL to detect fraudulent credit card transactions and provides actionable insights into transaction patterns and customer behavior. It’s a useful tool for detecting fraud in large datasets.

