import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# User inputs for network configuration
print("Configure your feedforward neural network:")
input_dim = int(input("Enter the input dimension: "))
output_dim = int(input("Enter the output dimension: "))
layers = int(input("Enter the number of hidden layers: "))

# Initialize the model
model = Sequential()

# Input layer
model.add(Dense(
    units=int(input(f"Enter the number of neurons for layer 1: ")),
    activation=input(f"Enter the activation function for layer 1 (e.g., relu, sigmoid, tanh): "),
    input_dim=input_dim
))

# Hidden layers
for i in range(2, layers + 1):
    model.add(Dense(
        units=int(input(f"Enter the number of neurons for layer {i}: ")),
        activation=input(f"Enter the activation function for layer {i} (e.g., relu, sigmoid, tanh): ")
    ))

# Output layer
model.add(Dense(units=output_dim, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
print("\nModel summary:")
model.summary()

# Generate random dataset for demonstration
print("\nGenerating a random dataset for training...")
samples = int(input("Enter the number of samples to generate: "))
X = np.random.rand(samples, input_dim)  # Random input data
Y = tf.keras.utils.to_categorical(np.random.randint(output_dim, size=(samples, 1)), num_classes=output_dim)  # Random labels

# Train the model
epochs = int(input("Enter the number of epochs for training: "))
model.fit(X, Y, epochs=epochs, batch_size=32)

# Test the model
print("\nTesting the model:")
test_samples = int(input("Enter the number of test samples to generate: "))
X_test = np.random.rand(test_samples, input_dim)  # Random test data
Y_test = tf.keras.utils.to_categorical(np.random.randint(output_dim, size=(test_samples, 1)), num_classes=output_dim)  # Random test labels

loss, accuracy = model.evaluate(X_test, Y_test, verbose=0)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")

# Save the model
save_model = input("Do you want to save the model? (yes/no): ").lower()
if save_model == 'yes':
    model.save("feedforward_model.h5")
    print("Model saved as 'feedforward_model.h5'")
