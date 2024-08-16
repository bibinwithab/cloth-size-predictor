import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('./data.csv')

df['Size_num'] = df['Size'].map({
    'XS': 0,
    'S': 1,
    'M': 2,
    'L': 3,
    'XL': 4
})

x = df[['Chest_min', 'Chest_max', 'Length_min', 'Length_max', 'Sleeve_length_min', 'Sleeve_length_max', 'Sleeve_open_min', 'Sleeve_open_max']]
y = df['Size_num']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy}")

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

user_chest_size = float(input("Enter chest size: "))
user_length = float(input("Enter length: "))
user_sleeve_length = float(input("Enter sleeve length: "))
user_sleeve_open = float(input("Enter sleeve open: "))

for i, row in df.iterrows():
    if (row['Chest_min'] <= user_chest_size <= row['Chest_max'] and
        row['Length_min'] <= user_length <= row['Length_max'] and
        row['Sleeve_length_min'] <= user_sleeve_length <= row['Sleeve_length_max'] and
        row['Sleeve_open_min'] <= user_sleeve_open <= row['Sleeve_open_max']):
        suggested_size = row['Size']
        print(f"Suggested Size: {suggested_size}")
        break
