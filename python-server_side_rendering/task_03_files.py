from flask import Flask, render_template
from flask import request
import json
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    DEFAULT_SOURCE = os.getenv('SOURCE', 'csv')
    source = request.args.get('source', DEFAULT_SOURCE)
    product_id = request.args.get('id', type=int)

    if source == 'json':
        with open('products.json', 'r') as file:
            products = json.load(file)

    elif source == 'csv':
        products = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        filtered_products = []
        for product in products:
            if product['id'] == product_id:
                filtered_products.append(product)
       
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        else:
            products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)