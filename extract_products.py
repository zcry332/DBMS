import mysql.connector
import csv

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'kula1987',  # Replace with your MySQL password
    'database': 'HUANG_airsupply'
}

try:
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # SQL query to get product data with vendor information
    query = """
    SELECT 
        p.ProductID,
        p.ProductName,
        CONCAT(p.ProductName, ' from ', v.VendorName) as ProductDescription,
        p.ProductPrice,
        v.VendorName
    FROM 
        Products p
    JOIN 
        Vendors v ON p.VendorID = v.VendorID
    ORDER BY 
        p.ProductID
    """

    # Execute the query
    cursor.execute(query)
    results = cursor.fetchall()

    # Write results to CSV file
    with open('HUANG_products.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write header
        csvwriter.writerow(['ProductID', 'ProductName', 'ProductDescription', 'ProductPrice', 'VendorName'])
        
        # Write data
        for row in results:
            csvwriter.writerow(row)

    print("Data successfully written to HUANG_products.csv")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Database connection closed")