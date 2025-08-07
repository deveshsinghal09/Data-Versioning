import pandas as pd
import os

#create a DataFrame with coulmn names
data={'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],    
        'City': ['New York', 'Los Angeles', 'Chicago']
        }
df=pd.DataFrame(data)

## Add a new row using a dictionary
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")