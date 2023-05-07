import tensorflow as tf


def train_recommendation_engine(x_train, y_train, x_test, y_test, num_features, num_classes):
    # Define the model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(num_features,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

    return model


# Example usage:
# model = train_recommendation_engine(x_train, y_train, x_test, y_test, num_features, num_classes)