```python
# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd

# Load the environmental data
climate_data = pd.read_csv('climate_data.csv')
air_quality_data = pd.read_csv('air_quality_data.csv')
biodiversity_data = pd.read_csv('biodiversity_data.csv')

# Load the environmental impact assessments
climate_impact = pd.read_csv('climate_impact.csv')
air_quality_impact = pd.read_csv('air_quality_impact.csv')
biodiversity_impact = pd.read_csv('biodiversity_impact.csv')

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the data page
@app.route('/data')
def data():
    return render_template('data.html', climate_data=climate_data, air_quality_data=air_quality_data, biodiversity_data=biodiversity_data)

# Define the route for the impact page
@app.route('/impact')
def impact():
    return render_template('impact.html', climate_impact=climate_impact, air_quality_impact=air_quality_impact, biodiversity_impact=biodiversity_impact)

# Define the route for the recommendations page
@app.route('/recommendations')
def recommendations():
    # Load the recommendations
    recommendations = pd.read_csv('recommendations.csv')
    return render_template('recommendations.html', recommendations=recommendations)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
