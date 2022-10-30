import random, json, pickle
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensofrlow.kearas.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizoers import SGD


# pip install --upgrade tensorflow
# conda create -n myenv python=3.8.5
# conda activate myenv


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
print(f'[+] Intents {intents}')

words = []
classes = []
documents = []
ignore_letters = ["?","!",".",","]

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            print(f'[-] Tag not found in Class')
            classes.append(intent['tag'])



## preprocess and remove duplicates
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))



print(documents)
print(f'[+] Words as a SET \n{words}')
print(f'[+] CLASSES as a SET \n{classes}')
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

print(f'[+] Serialized Words \n{words}')



training = []
output_empty = [0] * len(classes) ## creates a template of 0s with the len of classes
print(output_empty)
training.append(['bag'])
print('Training', training)


for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(documents[1])] = 1
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)



### TRAINING X/Y TEST
train_x = list(training[:,0])
train_y = list(training[:,1])
print(f'[+] [TRAIN_X] \n {train_x}')
print(f'[+] [TRAIN_Y] \n {train_y}')
print(f'[+] [CURRENTLY-TRAINING] \n {training}')
output_row = list(output_row)
print(f'[+] Output Empty \n{output_empty}')

#### BUILD MODEL ####
## neural network
# 1- dense layer with input dependent on lenght of x training data
# 2- Hidden layer set at half the input layers
# 3-
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activiation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(Ir=.01, decay=1e-6, momentum = 0.9, neterov=True)
model.compile(loss='categorical crossentropy', optimizer='sgd', metrics=['accuracy'])


##### Training Model ######
## Training - epochs set to 200 (how many tiems image is displayed)
#
# set histogram to

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=2)
model.save('chatbot model.model')
hist = model.fit(np.array(train_x), np.array(train_y))
print(f'[+] Training Complete')
model.save('chatbotmodel.h5', hist)
print('[+] Done')

