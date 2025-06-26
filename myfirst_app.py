import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Data Plotter")
st.write("Adjust the slider to change the number of data points.")

# Create a slider widget
num_points = st.slider(
    "Number of Data Points", # Label for the slider
    min_value=10,            # Minimum value
    max_value=200,           # Maximum value
    value=100,               # Default starting value
    step=10                  # Increment step
)

# Generate some random data based on the slider value
data = pd.DataFrame({
    'x': np.arange(num_points),
    'y': np.random.randn(num_points).cumsum() # Cumulative sum to make it look like a trend
})

# Display the data as a table (optional)
st.subheader("Raw Data:")
st.dataframe(data.head()) # Show only the first few rows

# Plot the data using Matplotlib
st.subheader("Data Plot:")
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title(f"Random Walk with {num_points} Points")
st.pyplot(fig) # Display the Matplotlib figure in Streamlit

st.write("---")
st.info("This app was created using Streamlit!")