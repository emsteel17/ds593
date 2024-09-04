import sqlite3
import csv

def import_csv_to_sqlite(csv_file, db_name):
    # Connect to the SQLite database (or create it)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Read the CSV file to get column names and data
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # First row as column names
        
        # Create a table with columns based on the headers
        columns = ', '.join([f'"{header}" TEXT' for header in headers])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS health_events ({columns});")
        
        # Insert the data into the table
        for row in reader:
            placeholders = ', '.join(['?'] * len(row))
            cursor.execute(f"INSERT INTO health_events VALUES ({placeholders});", row)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Data imported successfully into {db_name}.")

# Run the function
csv_file = 'funny_epidemiological_events.csv'  # Replace with your actual CSV file name
db_name = 'health_events_data.db'

import_csv_to_sqlite(csv_file, db_name)
