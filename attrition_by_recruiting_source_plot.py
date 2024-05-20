import pandas as pd
from plotnine import ggplot, aes, geom_bar, theme_minimal, labs

# Read the data from CSV to a DataFrame
recruitment_data = pd.read_csv('recruitment_data.csv')

# Plot attrition numbers by recruiting source
attrition_plot = (
    ggplot(recruitment_data, aes(x='recruiting_source', fill='factor(attrition)')) +
    geom_bar(stat='count') +
    theme_minimal() +
    labs(title='Attrition Numbers by Recruiting Source', x='Recruiting Source', y='Number of Candidates', fill='Attrition')
)

print(attrition_plot)