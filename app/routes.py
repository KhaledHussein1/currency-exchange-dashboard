from flask import Blueprint, render_template
import requests
import plotly
import plotly.express as px
import json

main = Blueprint('main', __name__)

# Obtain a key from https://openexchangerates.org/


@main.route('/')
def index():
    response = requests.get(f'https://openexchangerates.org/api/currencies.json')
    data = response.json()

    return render_template('index.html', currency=data)


@main.route('/historical/<date>')
def historical(date):
    response = requests.get(f'https://openexchangerates.org/api/historical/{date}.json?app_id={API_KEY}')
    data = response.json()['rates']
    fig = px.line(
        x=list(data.keys()), 
        y=list(data.values()), 
        title=f"Exchange Rates on {date}",
        labels={'x': 'Currency', 'y': 'Exchange Rate'},
        log_y=True
    )

    # Update the layout to center the title
    fig.update_layout(
        title={
            'text': f"Exchange Rates on {date}",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_tickangle=-45,
        margin=dict(l=1, r=1, t=70, b=60),
        xaxis_tickfont_size=11,
        autosize=True,
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Fetch the list of currencies again, as it's needed for the template
    currency_response = requests.get(f'https://openexchangerates.org/api/currencies.json')
    currency_data = currency_response.json()

    return render_template('index.html', plot_div=graphJSON, currency=currency_data)

