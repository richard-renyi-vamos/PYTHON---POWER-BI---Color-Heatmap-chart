import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

# Sample dataset
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

# Pivot the data for heatmap
heatmap_data = df.pivot_table(index='Category', aggfunc='mean')

# Create heatmap trace
heatmap_trace = go.Heatmap(
    z=[heatmap_data['Value']],
    x=heatmap_data.columns,
    y=heatmap_data.index,
    colorscale='Viridis'  # You can change the color scale as needed
)

# Define layout
layout = go.Layout(
    title='Color Heatmap Chart',
    xaxis=dict(title='X-axis'),
    yaxis=dict(title='Y-axis')
)

# Create figure
fig = go.Figure(data=[heatmap_trace], layout=layout)

# Save the figure as HTML file
pyo.plot(fig, filename='color_heatmap.html')
