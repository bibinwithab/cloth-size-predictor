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

# Define features and target variable
x = df[['Chest_min', 'Chest_max', 'Length_min', 'Length_max', 'Sleeve_length_min', 'Sleeve_length_max', 'Sleeve_open_min', 'Sleeve_open_max']]
y = df['Size_num']

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(x_train, y_train)

# Evaluate the model
accuracy = model.score(x_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Input user's measurements
user_chest_size = int(input("Enter chest size: "))
user_length = int(input("Enter length: "))
user_sleeve_length = int(input("Enter sleeve length: "))
user_sleeve_open = int(input("Enter sleeve open: "))

user_input = pd.DataFrame([{
    'Chest_min': user_chest_size,
    'Chest_max': user_chest_size, 
    'Length_min': user_length,
    'Length_max': user_length,
    'Sleeve_length_min': user_sleeve_length,
    'Sleeve_length_max': user_sleeve_length,
    'Sleeve_open_min': user_sleeve_open,
    'Sleeve_open_max': user_sleeve_open
}])

predicted_size_num = model.predict(user_input)[0]
predicted_size = df[df['Size_num'] == predicted_size_num]['Size'].values[0]

print(f"Suggested Size: {predicted_size}")
