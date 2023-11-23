import pandas as pd
starting_budget = 73.9
reduction_percentage = 0.008 

start_date = pd.to_datetime('2019-07-01')  
end_date = df['Date'].max()  
dates = pd.date_range(start=start_date, end=end_date, freq='D')
years_passed = (dates.year - start_date.year) + (dates.month >= start_date.month)
budget_values = starting_budget * (1 - reduction_percentage) ** years_passed