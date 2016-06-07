from DataModel import DataModel
from keras.models import Model, Sequential
from keras.layers import Input, Dense
from keras.layers.recurrent import SimpleRNN
from keras.callbacks import EarlyStopping
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

NUM_EPOCH = 40
HIDDEN_SIZE = 30

def create_rnn_model(input_size, output_size):
    """
    Creates a simple neural architecture.
    """
    
    model = Sequential()
    model.add(SimpleRNN(output_size, input_dim=input_size))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def create_one_layer_tanh_model(input_size, output_size):
    """
    Creates a one layer neural architecture.
    """
    
    model = Sequential()
    model.add(Dense(HIDDEN_SIZE, activation='tanh', input_shape=(input_size,)))
    model.add(Dense(output_size, activation='softmax'))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def create_relu_sigmoid_model(input_size, output_size):
    """
    Creates a one layer neural architecture.
    """
    
    model = Sequential()
    model.add(Dense(HIDDEN_SIZE, activation='sigmoid', input_shape=(input_size,)))
    model.add(Dense(HIDDEN_SIZE/2, activation='relu'))
    model.add(Dense(output_size, activation='softmax'))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return model


def create_one_layer_sigmoid_model(input_size, output_size):
    """
    Creates a one layer neural architecture.
    """
    
    model = Sequential()
    model.add(Dense(HIDDEN_SIZE, activation='sigmoid', input_shape=(input_size,)))
    model.add(Dense(output_size, activation='softmax'))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def create_simple_model(input_size, output_size):
    """
    Creates a simple neural architecture.
    """
    
    model = Sequential()
    model.add(Dense(output_size, activation='softmax', input_shape=(input_size,)))
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def evaluate_model(model, data_model, model_name):
    """
    Evaluates a given a model
    """
    print "\n\nRunning", model_name
    early_stopping = EarlyStopping(monitor='val_loss', patience=2)

    hist = model.fit(data_model.train_X, data_model.train_y, nb_epoch=NUM_EPOCH, validation_split=0.2, callbacks=[early_stopping])
    score = model.evaluate(data_model.test_X, data_model.test_y)

    print model_name, 'Test Accuracy:', score[1]

    return hist.history

def main():
    print "Loading data..."
    data_model = DataModel()
    input_size = len(data_model.top_words)
    output_size = len(data_model.get_genres())
   
    simple_history = evaluate_model(create_simple_model(input_size, output_size), data_model, "Simple")
    tanh_history = evaluate_model(create_one_layer_tanh_model(input_size, output_size), data_model, "One Layer tanh")
    sigmoid_history = evaluate_model(create_one_layer_sigmoid_model(input_size, output_size), data_model, "One Layer sigmoid")
    relu_sigmoid_history = evaluate_model(create_relu_sigmoid_model(input_size, output_size), data_model, "RELU sigmoid")

    sigmoid_epochs = [i for i in range(1, len(sigmoid_history['loss']) + 1)]
    plt.plot(sigmoid_epochs, sigmoid_history['val_acc'])
    plt.title('Validation Accuracy Over Time')
    plt.ylabel('Validation Accuracy')
    plt.xlabel('Epochs')
    plt.savefig('One_Sigmoid_Val_Acc.png')
    #plt.title('Loss and Accuracy History')


if __name__ == '__main__':
    main()

