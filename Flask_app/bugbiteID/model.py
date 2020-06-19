# this py file preprocess the uploaded file to the right size, and get the response for prediction from TF serving

import tensorflow as tf
import numpy as np

SIZE=150

model = tf.keras.models.load_model('/home/eyan/Desktop/bug_bite_old/models/8_class_mixed7_79p.h5')

CLASSES = ['ants','bed_bugs','chiggers','fleas','mosquitos','no_bites','spiders','ticks']

def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.inception_v3.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    result = model.predict(image)
    pred = np.argmax(result[0])
    # output the name of the class
    class_name = CLASSES[pred]
    return class_name