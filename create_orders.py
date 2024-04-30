import pandas as pd
from datetime import timedelta, date
import random

# Function to generate random orders
def generate_orders(num_orders, num_products, start_date):
    orders = []
    for i in range(1, num_orders + 1):
        product_id = random.randint(1, num_products)
        quantity = random.randint(1, 5)
        order_date = start_date + timedelta(days=random.randint(0, 70))
        orders.append({
            'id': i,
            'product_id': product_id,
            'quantity': quantity,
            'order_date': order_date
        })
    return orders

# Main function to generate and save multiple CSV files
def main():
    # Settings
    num_orders_per_file = 10
    num_products = 6
    start_date = date(2023, 4, 1)
    num_files = 10

    for file_number in range(1, num_files + 1):
        # Generate orders
        orders = generate_orders(num_orders_per_file, num_products, start_date)
        
        # Create a DataFrame
        orders_df = pd.DataFrame(orders)

        # Save to CSV
        filename = f'orders/order_number_{file_number}.csv'
        orders_df.to_csv(filename, index=False)
        print(f'Saved {filename}')

# Run the main function
if __name__ == "__main__":
    main()
