from DataModel import DataModel
from keras.models import Model, Sequential
from keras.layers import Input, Dense

NUM_EPOCH = 10

def create_one_layer_model(input_size, output_size):
    """
    Creates a one layer neural architecture.
    """
    
    model = Sequential()
    model.add(Dense(input_size/2, activation='sigmoid', input_shape=(input_size,)))
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
    model.fit(data_model.train_X, data_model.train_y, nb_epoch=NUM_EPOCH)
    score = model.evaluate(data_model.test_X, data_model.test_y)

    print model_name, 'Test Accuracy:', score[1]


def main():
    print "Loading data..."
    data_model = DataModel()
    input_size = len(data_model.top_words)
    output_size = len(data_model.get_genres())
   
    evaluate_model(create_simple_model(input_size, output_size), data_model, "Simple")
    evaluate_model(create_one_layer_model(input_size, output_size), data_model, "One Layer")


if __name__ == '__main__':
    main()

