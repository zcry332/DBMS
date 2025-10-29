import mysql.connector
import pandas as pd

def fetch_products():
    try:
        # Establish database connection
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='kula1987',  # Add your MySQL password here if you have set one
            database='HUANG_airsupply'
        )

        if connection.is_connected():
            # Create cursor and execute query
            cursor = connection.cursor()
            
            # Query to get product information including vendor name
            query = """
                SELECT 
                    p.ProductID,
                    p.ProductName,
                    CONCAT(p.ProductName, ' from ', v.VendorName) as product_description,
                    p.ProductPrice as price,
                    v.VendorName
                FROM Products p
                JOIN Vendors v ON p.VendorID = v.VendorID
                ORDER BY p.ProductID
            """
            
            cursor.execute(query)
            
            # Fetch all results
            results = cursor.fetchall()
            
            # Convert to DataFrame
            df = pd.DataFrame(results, columns=[
                'Product ID',
                'Product Name',
                'Product Description',
                'Price',
                'Vendor Name'
            ])
            
            # Save to CSV
            df.to_csv('HUANG_products.csv', index=False)
            print("Data successfully exported to HUANG_products.csv")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Database: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    fetch_products() 