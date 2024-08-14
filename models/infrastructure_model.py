import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Dropout, Input
from tensorflow.keras.models import Model

def build_infrastructure_model(input_shape):
    inputs = Input(shape=input_shape)
    x = Flatten()(inputs)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.5)(x)
    output = Dense(2, activation='softmax')(x)  # Binary classification (Suitable/Not Suitable)
    model = Model(inputs=inputs, outputs=output)

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    input_shape = (128, 128, 3)
    model = build_infrastructure_model(input_shape)
    # Load and preprocess your dataset here
    # Train the model
    # Save the trained model
