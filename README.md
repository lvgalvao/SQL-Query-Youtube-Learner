# SQL Query Youtube Learner

This Python project helps users find resources to learn about the main topic of a given SQL query. It first extracts the main topic from the query using OpenAI's GPT-3.5-turbo and then searches YouTube for relevant videos to help the user learn more about the topic.

## Features

- Extracts the main topic from an SQL query using OpenAI GPT-3.5-turbo.
- Searches YouTube for the top video resources related to the main topic.
- Displays the video titles and URLs for user convenience.  

## Installation
To install the project, you need to have Python 3.10 and Poetry installed. Follow these steps:

Clone the repository:

```bash
git clone https://github.com/your-repo/youtube-api.git
cd youtube-api
```

Install the dependencies using Poetry:

```bash
poetry install
```

## Usage

After installing the dependencies, you can use the project as follows:

Activate the virtual environment:

```bash
poetry shell
```

Into the __init__ change de query, you can put a big one:

```python
query = """
WITH 
    sales_data AS (
        SELECT
            s.order_date,
            s.product_id,
            p.product_name,
            p.product_category,
            s.quantity,
            s.price_per_unit,
            s.discount_percentage,
            s.tax_rate,
            (s.quantity * s.price_per_unit * (1 - s.discount_percentage) * (1 + s.tax_rate)) AS total_sales
        FROM
            sales s
            JOIN products p ON s.product_id = p.product_id
    ),
    sales_totals AS (
        SELECT
            order_date,
            SUM(total_sales) AS total_sales,
            SUM(quantity) AS total_units_sold,
            COUNT(DISTINCT product_id) AS total_products_sold,
            AVG(total_sales) AS avg_sale_per_order
        FROM
            sales_data
        GROUP BY
            order_date
    ),
    category_sales AS (
        SELECT
            product_category,
            order_date,
            SUM(total_sales) AS total_sales,
            SUM(quantity) AS total_units_sold
        FROM
            sales_data
        GROUP BY
            product_category,
            order_date
    ),
    category_totals AS (
        SELECT
            product_category,
            SUM(total_sales) AS total_sales,
            SUM(total_units_sold) AS total_units_sold,
            COUNT(DISTINCT order_date) AS total_days_sold,
            AVG(total_sales) AS avg_sales_per_day
        FROM
            category_sales
        GROUP BY
            product_category
    )
SELECT
    c.product_category,
    c.total_sales AS category_total_sales,
    c.total_units_sold AS category_total_units_sold,
    c.total_days_sold AS category_total_days_sold,
    c.avg_sales_per_day AS category_avg_sales_per_day,
    s.total_sales AS overall_total_sales,
    s.total_units_sold AS overall_total_units_sold,
    s.total_products_sold AS overall_total_products_sold,
    s.avg_sale_per_order AS overall_avg_sale_per_order
FROM
    category_totals c
    JOIN sales_totals s ON c.product_category = s.product_category
ORDER BY
    overall_total_sales DESC;"""
```

Run the main script

```bash
python __init__.py
```

The script will extract the main topic from the given SQL query, search YouTube for relevant videos, and display the video titles and URLs.

Example of output

```doc
The topic is "SQL query for Sales Analysis"

- Learn SQL for Data Analysis in one hour (with sample dataset + 50 queries) https://www.youtube.com/watch?v=l8DCPaHc5TQ

- SQL for Marketers and Marketing Analysts https://www.youtube.com/watch?v=yW3HOvyZHbo

- Advanced SQL Tutorial | Subqueries https://www.youtube.com/watch?v=m1KcNV-Zhmc
```


