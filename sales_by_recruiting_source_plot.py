import pandas as pd
from plotnine import ggplot, aes, geom_bar, theme, element_text

# Read the dataset
data = pd.read_csv('recruitment_data.csv')

# Check the first few rows of the DataFrame
print(data.head())

# Plot sales by recruiting source
sales_plot = (
    ggplot(data, aes(x='recruiting_source', y='sales_quota_pct', fill='recruiting_source')) +
    geom_bar(stat='identity') +
    theme(axis_text_x=element_text(angle=45, hjust=1))
)

# Draw the plot
sales_plot.draw()
