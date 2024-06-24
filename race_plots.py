import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/ACS_50k.csv'
df = pd.read_csv(file_path)

# Plot the distribution of different races (RAC1P column)
race_counts = df['RAC1P'].value_counts()

plt.figure(figsize=(10, 6))
bar_plot = race_counts.plot(kind='bar')
plt.xlabel('Race Code')
plt.ylabel('Count')
plt.title('Distribution of Different Races in the ACSIncome Dataset')
plt.xticks(rotation=0)

# Add count labels above the bars
for i, count in enumerate(race_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')





plt.show()
