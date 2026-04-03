# Student Performance Analysis

# step1: import pandas library
import pandas as pd
import numpy as np

data = {
    'Name': ['Sanket', 'Sagar', 'Swapnil', 'Swapnali', 'Sanket'],
    'Math': [80, 90, 85, 95, 88],
    'Science': [70, 80, 75, 85, 82],
    'English': [60, 70, 65, 75, 72]
}

df = pd.DataFrame(data)
print(df)

# step2: Add new column 'Total' and 'Average'
df['Total'] = df['Math'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3
print(df)

# step3: find top performer
top_student = df.sort_values("Total", ascending=False).iloc[0]
print("Top Performer:\n", top_student)

# step4: using NumPy for statistical analysis
avg_marks = np.mean(df['Average'])
print("Average marks:", avg_marks)

# step5: filter students who scored above average
high_performers = df[df['Average'] > 75]
print("High Performers:", high_performers)

low_performers = df[df['Average'] <70]
print("Low Performers:", low_performers)

