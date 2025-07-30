# A simple script to perform basic analysis on a list of sales records.

def analyze_sales_data(records: list[dict]) -> dict:
    """
    Processes a list of sales records and calculates key metrics.

    Each record is expected to be a dictionary with 'product_id', 'quantity', and 'price'.
    
    Args:
        records (list[dict]): A list of sales records.

    Returns:
        A dictionary containing the analysis results:
        - total_revenue
        - total_items_sold
        - best_selling_product (ID)
    """
    if not records:
        return {
            "total_revenue": 0,
            "total_items_sold": 0,
            "best_selling_product": None
        }

    total_revenue = 0
    total_items_sold = 0
    product_sales = {} # To track sales per product

    for record in records:
        sale_value = record.get('quantity', 0) * record.get('price', 0)
        total_revenue += sale_value
        total_items_sold += record.get('quantity', 0)
        
        product_id = record.get('product_id')
        if product_id:
            product_sales[product_id] = product_sales.get(product_id, 0) + record.get('quantity', 0)

    # Find the best-selling product
    if not product_sales:
        best_selling_product = None
    else:
        best_selling_product = max(product_sales, key=product_sales.get)

    return {
        "total_revenue": round(total_revenue, 2),
        "total_items_sold": total_items_sold,
        "best_selling_product": best_selling_product
    }

# This part below should NOT be summarized as it's just an example execution
if __name__ == "__main__":
    sample_sales = [
        {"product_id": "A101", "quantity": 5, "price": 10.00},
        {"product_id": "B202", "quantity": 2, "price": 25.50},
        {"product_id": "A101", "quantity": 10, "price": 10.00},
        {"product_id": "C303", "quantity": 1, "price": 150.75},
        {"product_id": "B202", "quantity": 3, "price": 25.50},
    ]
    
    analysis = analyze_sales_data(sample_sales)
    print("Sales Analysis Report:")
    print(f"  Total Revenue: ${analysis['total_revenue']:.2f}")
    print(f"  Total Items Sold: {analysis['total_items_sold']}")
    print(f"  Best Selling Product: {analysis['best_selling_product']}")