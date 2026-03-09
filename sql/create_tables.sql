CREATE TABLE fact_sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    sales_amount FLOAT,
    order_date DATE
);

CREATE TABLE dim_customer (
    customer_id INT,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);
