# this py file preprocess the uploaded file to the right size, and get the response for prediction from TF serving

import tensorflow as tf
import numpy as np
import json
import requests

SIZE=299
MODEL_URI='http://localhost:8501/v1/models/bug_model:predict'
CLASSES = ['ants', 'chiggers', 'rash', 'negative', 'bed_bugs', 'spiders','ticks']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({
        'instances': image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    result = json.loads(response.text)
    #print(result)
    prediction = np.squeeze(result['predictions'][0])
    # argmax gets the class with the highest prob
    pred = np.argmax(prediction)
    # output the name of the class
    class_name = CLASSES[pred]
    return class_name