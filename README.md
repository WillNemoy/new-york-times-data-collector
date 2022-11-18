# new-york-times-data-collector
Collect New York Times article data based on keywords.


## Setup


Create and activate a virtual environment:

```sh
conda create -n nydata-env python=3.8

conda activate nydata-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage (i.e. `ALPHAVANTAGE_API_KEY`).

Also sign up for the [SendGrid Service](https://sendgrid.com/), verify your single sender address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API Key (i.e. `SENDGRID_API_KEY`). See these [setup notes](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#setup) for more details.

Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
SENDER_EMAIL_ADDRESS="you@example.com"
SENDGRID_API_KEY="__________"
```


## Usage

Run the unemployment report:

```sh
python app.py
```




