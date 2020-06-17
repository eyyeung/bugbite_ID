# BugBite ID
* Description: An web application to help you identify what bugs bite you through an image of your bug bite and suggests bug-based and situation-based products and pest control companies

# Folders
* Resources :
    * contains Jupyter notebooks for web scraping for images, products, and pest control companies and for making SQLite database
    * folders:
        * cropped: contains all the images used for training and validation in their inidividual folders
        * webpage_resources: csv files containing information about products, bug bite information, etc for making the SQLite databases

* TensorFlow_Keras_LIME: 
    * Jupyter notebooks for training and saving TF Keras model, looking at misidentifications, visualizing intermediate layers, and explaining the classication through LIME

* Flask_app:
    * bugbiteID- the Flask app