import requests
from bs4 import BeautifulSoup

# Define the URL of the site to scrape
url = 'https://oettv.xttv.at/ed/index.php?lid=7298'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract table data
    table = soup.find('table')  # Assuming the main data is in a table
    if table:
        headers = [header.get_text() for header in table.find_all('th')]
        rows = table.find_all('tr')
        
        table_data = []
        for row in rows:
            columns = row.find_all('td')
            if columns:  # Ensure the row contains table data
                row_data = [column.get_text().strip() for column in columns]
                table_data.append(row_data)
        
        # Print headers and rows
        print("Headers:", headers)
        for row_data in table_data:
            print("Row data:", row_data)
    
    else:
        print("No table found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Optionally, write the gathered data to a file
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    # Example: Write headers to the file
    file.write('Headers:\n')
    file.write(', '.join(headers) + '\n')
    
    # Example: Write rows to the file
    file.write('\nRows:\n')
    for row_data in table_data:
        file.write(', '.join(row_data) + '\n')