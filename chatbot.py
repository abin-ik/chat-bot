import json  # to read json files
import random #to read random files
from sklearn.feature_extraction.text import CountVectorizer # converts text into numbers
from sklearn.naive_bayes import MultinomialNB # simple bediner friendly ai model

with open ("intents.json") as file :
    data = json.load(file) 

x_train = []
y_train = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        x_train.append(pattern)
        y_train.append(intent["tag"])

vectorizer = CountVectorizer()
x_train_vectors = vectorizer.fit_transform(x_train)

model = MultinomialNB()
model.fit(x_train_vectors,y_train)

def chatbot_response(user_input):
    user_vector = vectorizer.transform([user_input])
    predicted_tag = model.predict(user_vector)[0]

    for intent in data["intents"]:

        if intent["tag"]  == predicted_tag:
            return random.choice(intent["responses"])
        
