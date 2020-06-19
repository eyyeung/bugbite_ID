# BugBite ID
* Description: An web application to help you identify what bugs bite you through an image of your bug bite and suggests bug-based and situation-based products and pest control companies

# Folders
* Resources :
    * contains Jupyter notebooks for web scraping for images, products, and pest control companies and for making SQLite database
    * folders:
        * cropped: contains all the images used for training and validation in their inidividual folders
        * webpage_resources: csv files containing information about products, bug bite information, etc for making the SQLite databases

* Simple_models:
    * Jupyter notebooks for training simple Logistic Regression and CNN model for bug bite image classification

* TensorFlow_Keras_LIME: 
    * Jupyter notebooks for training and saving TF Keras model, looking at misidentifications, visualizing intermediate layers, and explaining the classication through LIME

* Flask_app:
    * bugbiteID- the Flask app to identify bugbite based on an image and provide bug-specific, symtom-specific information
    * TF Keras model is loaded in the 'model.py' file, change the file path to the path of the model:
        * To download the TF Keras model, click <a href="https://drive.google.com/file/d/1XYy3ltdV0zzBVYRU2ggnp4MsNvnlWriX/view?usp=sharing">here</a>
    * To run the Flask app, run 'app.py'