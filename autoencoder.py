import tensorflow.keras as tk
import pandas as pd
import os
import matplotlib.pyplot as plt

# Prepare the data
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir += '/Data/'
data = pd.read_csv(dir + 'data.csv', index_col=0)
data.index = pd.to_datetime(data.index)
x_train = data

# Define the autoencoder architecture
input_dim = x_train.shape[1]
encoding_dim = 3
input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation='relu')(input_layer)
decoder = Dense(input_dim, activation='sigmoid')(encoder)

# Define the autoencoder model
autoencoder = Model(inputs=input_layer, outputs=decoder)

# Compile the model
autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder on the mixed dataset
autoencoder.fit(x_train, x_train, epochs=50, batch_size=32)

# Use the trained autoencoder to reconstruct the mixed dataset
reconstructions = autoencoder.predict(x_train)

# Calculate the reconstruction error (MSE) for each data point
mse = tf.keras.losses.mean_squared_error(x_train, reconstructions)
mse = mse.numpy()

# Split the data into normal and anomaly sets based on the reconstruction error
threshold = 0.01  # adjust this threshold as needed
is_anomaly = mse > threshold
x_normal = x_train[~is_anomaly]
anomalies = x_train[is_anomaly]
print(anomalies)
plt.figure(figsize=(15, 7))
fig, ax = plt.subplots()
ax.plot(data.index, data['D'], label='Time Series Data')
ax.scatter(anomalies.index, anomalies['D'], color='red', label='Anomalies')

plt.legend()
plt.savefig('autoencoder.jpg')
"""
# Fine-tune the autoencoder on the normal data only (optional)
autoencoder.fit(x_normal, x_normal, epochs=10, batch_size=32)

# Use the trained autoencoder to detect anomalies in new, unseen data
x_test = ...
reconstructions = autoencoder.predict(x_test)
mse = tf.keras.losses.mean_squared_error(x_test, reconstructions)
mse = mse.numpy()
is_anomaly = mse > threshold
x_anomaly = x_test[is_anomaly]
"""
