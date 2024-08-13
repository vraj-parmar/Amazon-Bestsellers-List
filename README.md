# Amazon Bestsellers List Scraper

## Overview

This project is a Python-based web scraper that extracts the top 100 bestselling beauty products from Amazon UK. It collects data such as product titles, ratings, prices, and URLs for the top products in the beauty category.

## Features

- Scrapes product information from the Amazon UK Bestsellers page.
- Extracts product titles, ratings, prices, and URLs.
- Handles multiple pages of listings.
- Saves the scraped data to a CSV file.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `pandas`

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vraj-parmar/Amazon-Bestsellers-List.git
   cd Amazon-Bestsellers-List
   ```

2. **Install Dependencies:**

   You can install the required Python packages using `pip`. It's recommended to use a virtual environment.

   ```bash
   pip install requests beautifulsoup4 pandas
   ```

## Usage

1. **Run the Notebook:**

   Open `Untitled.ipynb` in Jupyter Notebook or JupyterLab and execute the cells to run the web scraper.

2. **Data Output:**

   The script scrapes data from the Amazon UK Bestsellers page and saves it to a CSV file named `prod.csv` in the current directory.

   ```bash
   python Untitled.ipynb
   ```

## Code Overview

- **Fetching Data:**
  The script makes a GET request to the Amazon UK Bestsellers page using the `requests` library.

- **Parsing HTML:**
  It uses `BeautifulSoup` to parse the HTML content and extract product titles, ratings, prices, and URLs.

- **Data Extraction:**
  Functions are defined to extract specific data from the parsed HTML:
  - `get_all_stars()` - Extracts ratings.
  - `get_all_price()` - Extracts prices.
  - `get_all_url()` - Extracts product URLs.

- **Scraping Multiple Pages:**
  The `scrape_page()` function handles data extraction for multiple pages by iterating over page numbers.

- **Saving Data:**
  The scraped data is compiled into a pandas DataFrame and saved as `prod.csv`.

## Note

- The scraping logic is designed for the specific structure of Amazon's page. If Amazon changes their page structure, adjustments to the code may be necessary.
- The scraping of websites should be done respectfully and in accordance with the website's terms of service.
