import json
import random
import nltk
import string
import numpy as np
import pickle
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences

global responses, lemmatizer, tokenizer, le, model, input_shape
input_shape = 8

# import dataset answer
def load_response():
    global responses
    responses = {}
    with open('data\intents.json', encoding='utf-8') as content:
        data = json.load(content)
    for intent in data['intents']:
        responses[intent['tag']] = intent['responses']


# import model dan download nltk file
def preparation():
    load_response()
    global lemmatizer, tokenizer, le, model
    tokenizer = pickle.load(open('model/tokenizers.pkl', 'rb'))
    le = pickle.load(open('model\le.pkl', 'rb'))
    model = keras.models.load_model('model\chat_model.h5')
    lemmatizer = WordNetLemmatizer()
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

# hapus tanda baca
def remove_punctuation(text):
    text = [letters.lower() for letters in text if letters not in string.punctuation]
    text = ''.join(text)
    return text

# klasifikasi pertanyaan user
def predict(vector):
    output = model.predict(vector)
    output = output.argmax(axis=1)
    response_tag = le.inverse_transform(output)[0]
    return response_tag

# menghasilkan jawaban berdasarkan pertanyaan user
def generate_response(text):
    text = remove_punctuation(text)
    vector = tokenizer.texts_to_sequences([text])
    vector = pad_sequences(vector, maxlen=input_shape)
    response_tag = predict(vector)
    answer = random.choice(responses[response_tag])
    return answer
