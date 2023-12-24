```python
# Import necessary libraries
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load the environmental data
climate_data = pd.read_csv('climate_data.csv')
air_quality_data = pd.read_csv('air_quality_data.csv')
biodiversity_data = pd.read_csv('biodiversity_data.csv')

# Load the environmental impact assessments
climate_impact = pd.read_csv('climate_impact.csv')
air_quality_impact = pd.read_csv('air_quality_impact.csv')
biodiversity_impact = pd.read_csv('biodiversity_impact.csv')

# Function to calculate the impact score
def calculate_impact_score(actual_data, predicted_data):
    # Calculate the mean squared error between the actual and predicted data
    mse = mean_squared_error(actual_data, predicted_data)
    
    # Calculate the mean absolute error between the actual and predicted data
    mae = mean_absolute_error(actual_data, predicted_data)
    
    # The impact score is the average of the MSE and MAE
    impact_score = (mse + mae) / 2
    
    return impact_score

# Calculate the impact scores
climate_impact_score = calculate_impact_score(climate_data, climate_impact)
air_quality_impact_score = calculate_impact_score(air_quality_data, air_quality_impact)
biodiversity_impact_score = calculate_impact_score(biodiversity_data, biodiversity_impact)

# Print the impact scores
print('Climate Impact Score:', climate_impact_score)
print('Air Quality Impact Score:', air_quality_impact_score)
print('Biodiversity Impact Score:', biodiversity_impact_score)
```
