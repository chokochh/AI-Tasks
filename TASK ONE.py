import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print("Training images shape:", x_train.shape)
print("Testing images shape:", x_test.shape)

x_train = x_train / 255.0
x_test = x_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential([
    Flatten(input_shape=(28, 28)),   # Convert 28x28 image to 1D array
    Dense(128, activation='relu'),   # Hidden layer
    Dense(10, activation='softmax')  # Output layer for digits 0-9
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=5)

loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", accuracy)

prediction = model.predict(x_test[:1])

print("Predicted digit:", prediction.argmax())

