```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the environmental data
climate_data = pd.read_csv('climate_data.csv')
air_quality_data = pd.read_csv('air_quality_data.csv')
biodiversity_data = pd.read_csv('biodiversity_data.csv')

# Function to visualize data using Matplotlib
def visualize_data_matplotlib(data, title):
    data.plot(kind='line')
    plt.title(title)
    plt.show()

# Function to visualize data using Plotly
def visualize_data_plotly(data, title):
    fig = px.line(data_frame=data, title=title)
    fig.show()

# Visualize the environmental data
visualize_data_matplotlib(climate_data, 'Climate Data')
visualize_data_matplotlib(air_quality_data, 'Air Quality Data')
visualize_data_matplotlib(biodiversity_data, 'Biodiversity Data')

visualize_data_plotly(climate_data, 'Climate Data')
visualize_data_plotly(air_quality_data, 'Air Quality Data')
visualize_data_plotly(biodiversity_data, 'Biodiversity Data')
```

