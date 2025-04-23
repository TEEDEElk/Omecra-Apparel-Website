# filepath: app.py
# type: ignore
from flask import Flask, render_template
import random

app = Flask(__name__)

# Base name
base_name = "omecra"

# Domain extensions
extensions = [".com", ".in", ".co", ".net", ".apparel"]

# Function to generate a domain name
def generate_domain(base, extensions):
    # Randomly select an extension
    extension = random.choice(extensions)
    # Combine base name with the selected extension
    domain_name = base + extension
    return domain_name

@app.route('/')
def index():
    domains = [generate_domain(base_name, extensions) for _ in range(5)]
    return render_template('index.html', domains=domains)

if __name__ == '__main__':
    app.run(debug=True)