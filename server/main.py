import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv('./clothing_dataset.csv')

df.dropna(inplace=True)
df = df[df['Chest'] > 0]

df['Size_num'] = df['Size'].map({
    'XS': 0,
    'S': 1,
    'M': 2,
    'L': 3,
    'XL': 4,
    'XXL': 5
})

df['Chest_weighted'] = df['Chest'] * 2.0
df['Shoulder_weighted'] = df['Shoulder'] * 2.0  

x = df[['Chest_weighted', 'Shoulder_weighted', 'Front_Length', 'Sleeve_length']]
y = df['Size_num']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

label_encoder = LabelEncoder()
df['Size_encoded'] = label_encoder.fit_transform(df['Size'])

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred,
labels=[0, 1, 2, 3, 4, 5], target_names=['XS', 'S', 'M', 'L', 'XL', 'XXL']))

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

user_chest = float(input("Enter chest size: "))
user_shoulder = float(input("Enter shoulder size: "))
user_front_length = float(input("Enter front length: "))
user_sleeve_length = float(input("Enter sleeve length: "))

user_chest_weighted = user_chest * 2.0
user_shoulder_weighted = user_shoulder * 2.0

user_input = pd.DataFrame([{
    'Chest_weighted': user_chest_weighted,
    'Shoulder_weighted': user_shoulder_weighted,
    'Front_Length': user_front_length,
    'Sleeve_length': user_sleeve_length
}])

predicted_size_num = model.predict(user_input)[0]
predicted_size = df[df['Size_num'] == predicted_size_num]['Size'].values[0]

print(f"Suggested Size: {predicted_size}")
