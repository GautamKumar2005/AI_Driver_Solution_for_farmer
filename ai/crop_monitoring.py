import sys
import cv2
import numpy as np
import tensorflow as tf

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    model = tf.keras.models.load_model('crop_monitoring_model.h5')
    prediction = model.predict(image)
    return prediction

if __name__ == '__main__':
    image_path = sys.argv[1]
    image = preprocess_image(image_path)
    prediction = predict(image)
    result = {
        'health': float(prediction[0][0]),
        'growth_stage': float(prediction[0][1]),
        'nutrient_deficiency': float(prediction[0][2])
    }
    print(result)
