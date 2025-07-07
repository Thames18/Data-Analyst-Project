import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load CSV
df = pd.read_csv('data/customers.csv')
print("Data loaded:")
print(df.head())

# Simple stats
print("\nAverage age:", df['age'].mean())

# Save to SQLite
conn = sqlite3.connect('customers.db')
df.to_sql('customers', conn, if_exists='replace', index=False)
print("Data saved to SQLite database.")

# Simple plot
df['age'].hist()
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_distribution.png')
plt.show()

conn.close()
