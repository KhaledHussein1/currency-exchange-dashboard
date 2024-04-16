
# Currency Exchange Rates Dashboard

## Overview

Currency Exchange Dashboard is a Flask-based web application that provides real-time and historical currency exchange rates. Utilizing the Open Exchange Rates API, the application offers interactive visualizations with Plotly, catering to users interested in tracking currency market trends.

## Features

- Displays real-time currency exchange rates.
- Historical data visualization through interactive charts.
- Dynamic search and filtering of currencies.
- Responsive web interface designed for ease of use.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip and virtualenv

### Setup Instructions

1. **Clone the repository**
git clone https://github.com/KhaledHussein1 currency-exchange-dashboard.git
cd CurrencyDashboard

2. **Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install dependencies**
pip install -r requirements.txt

4. **Environment Variables**
Replace `ENTER_KEY_HERE` (in routes.py) with the actual API key from [Open Exchange Rates](https://openexchangerates.org/). This key is necessary to fetch the currency data.

### Running the Application

To run the application locally:
flask run

This will start the server on `http://localhost:5000`. Navigate to this URL in your web browser to view the application.

## Usage

Explore real-time and historical exchange rates through the dashboard. Use the date picker to view exchange rates from past dates and utilize the search function to filter through different currencies.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request, or create an issue to discuss the changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.