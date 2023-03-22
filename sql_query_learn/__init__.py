from search_youtube import search_youtube
from getAnswer import GetAnswer

query = """
Copy code
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

mainTopicToLearn = GetAnswer(query)

#Example usage: search for "cats" and print the video titles and URLs on separate lines
search_query = f"how to learn {mainTopicToLearn}"
max_results = 3
results_dict = search_youtube(search_query, max_results)

print(f"the main topic is {mainTopicToLearn}")
for video in results_dict['videos']:
    print(video['title'], video['video_url'])