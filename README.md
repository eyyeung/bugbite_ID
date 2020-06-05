# BugBite ID
* Description: An web application to help you identify what bugs bite you through an image of your bug bite

# Folders
* web_scraping :
    * contains Jupyter notebook for web scraping for images, products, and pest control companies
    * folders:
        * useful: contains all the images used for training and validation in their inidividual folders
        * national_records: contains ER visit for bug bites in the 2000s annually and monthly record
        * webpage_resources: bug bite relief products csv
            * others: bug_situation_treatment

* EDA_Preprocessing : 
    * Basic stats about the images Jupyter notebook

* TensorFlow_Keras: 
    * Jupyter notebooks for training TF Keras model and looking at misidentifications

* Flask_app:
    * tensorflow serving Jupyter notebook - run this to start TF serving
    * folders:
        * bugbiteID- the Flask app