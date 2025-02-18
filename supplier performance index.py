import pandas as pd

# Creating supplier data
supplier_data = {
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E'],
    'Number of Products Sold': [5000, 8000, 3000, 10000, 6000],
    'Revenue': [500000, 800000, 300000, 1000000, 600000],
    'Customer Feedback': [4.5, 3.8, 4.2, 4.7, 4.0],
    'Actual Delivery Time': [6, 5, 8, 5, 4],  # in days
    'Agreed-Upon Time': [5, 5, 5, 5, 5],  # in days
    'Conversion Rate': [0.4, 0.35, 0.3, 0.5, 0.38],
    'Return Rate': [0.1, 0.15, 0.05, 0.12, 0.08],  # as fraction
    'Years of Experience': [5, 8, 3, 10, 6]
}

# Defining the weights and scaling factors
scaling_factors = {
    'Sales Scaling Factor': 10000,
    'Revenue Scaling Factor': 1000000,
    'Delivery Scaling Factor': 3,
    'Return Scaling Factor': 0.2,
    'Years of Experience Scaling Factor': 10
}

weights = {
    'Sales Weight': 0.2,
    'Revenue Weight': 0.2,
    'Feedback Weight': 0.15,
    'Delivery Weight': 0.15,
    'Conversion Weight': 0.1,
    'Return Weight': 0.1,
    'Experience Weight': 0.1
}

# Calculate index values based on the algorithm
def calculate_index(row):
    sales_score = (row['Number of Products Sold'] / scaling_factors['Sales Scaling Factor']) * weights['Sales Weight']
    revenue_score = (row['Revenue'] / scaling_factors['Revenue Scaling Factor']) * weights['Revenue Weight']
    feedback_score = row['Customer Feedback'] * weights['Feedback Weight']
    
    delivery_score = max(0, 1 - (row['Actual Delivery Time'] - row['Agreed-Upon Time']) / scaling_factors['Delivery Scaling Factor']) * weights['Delivery Weight']
    
    conversion_score = row['Conversion Rate'] * weights['Conversion Weight']
    
    return_rate_score = max(0, 1 - row['Return Rate'] / scaling_factors['Return Scaling Factor']) * weights['Return Weight']
    
    experience_score = (row['Years of Experience'] / scaling_factors['Years of Experience Scaling Factor']) * weights['Experience Weight']
    
    # Total index value
    index_value = sales_score + revenue_score + feedback_score + delivery_score + conversion_score + return_rate_score + experience_score
    return index_value

# Create a DataFrame
df = pd.DataFrame(supplier_data)

# Apply the function to calculate index values
df['Performance Index'] = df.apply(calculate_index, axis=1)

df[['Supplier', 'Performance Index']]
