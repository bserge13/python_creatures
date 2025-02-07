import requests
from bs4 import BeautifulSoup

def print_character_grid(doc_url):
    # Step 1: Fetch the document content
    response = requests.get(doc_url)
    response.raise_for_status()  # Raise an error if the request fails
    html_content = response.text

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")  # Find the first table in the document

    # Step 3: Extract table rows
    grid_data = []
    for row in table.find_all("tr")[1:]:  # Skip the header row
        cols = row.find_all("td")
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        grid_data.append((x, y, char))

    # Step 4: Build the grid
    # Determine grid size based on max x and y values
    max_x = max(data[0] for data in grid_data)
    max_y = max(data[1] for data in grid_data)

    # Create an empty grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Populate the grid using x, y, and characters
    for x, y, char in grid_data:
        adjusted_y = max_y - y  # Reverse the y-axis to account for the flipped orientation
        grid[adjusted_y][x] = char

    # Step 5: Print the grid
    for row in grid:
        print("".join(row))

# Example usage
url = input('enter a google doc url: ')
print_character_grid(url)