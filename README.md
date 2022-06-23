## BookingGauger: Machine learning api for predicting number of accommodation days an online visitor will book.

## Overview

This project builds an Automated Machine Learning (AutoML) API and dash web application as an interface 
to request prediction of number of days to be booked for accommodation by a user. 


### Packages used for the Dash web application
The exact packages and version used found in UI/requirements.txt


### Packages used for AutoML API
The exact packages and version used are found in api/requirements.txt


### How the application works 

The dash web application provides a User Interface (UI) -- code in UI folder -- for selecting various variables for prediction.
When the button is clicked for prediction, all the inputs selected are retrieved and transformed (label encoding is to make categorical
variable acceptable in machine learning model). The inputs are used to make a request to the API. The API accepts the inputs and
pass them into the model to make a prediction and return a reponse to be displayed in a user friendly manner in the UI.

### How to run the AutoML API

Note that the AutoML API and dash app are independent of each other and can infact be treated as separate projects in their own right
despite their complementary role. For example, you can make request to the API for prediction in a notebook environment with 
the dash web application. However, for smooth workflow and offloading of all the grunt work, the User Interface (UI) provided by
the dash wep application is recommended to be used in making request.

By this both the API and the web application should be running at the same time.

The steps for running the API are as below

1. Create a virtual environment (replace 'project' with your prefreed pathname)

```
python3 -m venv project_env
```
 

3. Activate your virtual environment as follows

```
source project_env/bin/activate
```

3. Clone repository into the virtual environment created
With **_git already installed_**, run the command below in your terminal to get the code into your local environment

```
git clone git@github.com:agbleze/machine_learning_api.git
```

Within the the cloned repo, the folder api contains all the code to run the api. First, navigate to the api folder.
From the terminal run

```
cd api
```

4. Install packages used as follows

```
pip install -r requirements.txt
```

5. Run the API

```
python3 app.py
```

Now the api is running and request can be made to it. To do that, the dash app needs to be run and with the user interface provided, making prediction requests becomes easier. Note that the endpoint to the machine learning api is "/predict" and this has to be 
added to api url to successfully reach the prediction model.


### How to run the dash web application

The code for the web application is in the UI folder and infact can be easily run with same process used to run the api. The difference is that
the result this time round will be a nice user interface, you can play around with.

__Preferrably__, the dash app should be run separately in a different virtual environment. Just for clarity and to take note of subtle differences,
the steps are highlighted below

```
python3 -m venv ui_env
```

```
source ui_env/bin/activate
```

```
cd UI
```


```
pip install -r requirements.txt
```


```
python3 app.py
```


## Project description

The aim of this project is to predict the number of days that
customers are likely to book an accommodation for based on user bahaviour.
The end-user is an accommodation provider who sought to obtain
an intelligent tool that can enable the prediction of number of days that an online vistor will book for accommodation.
based on a number of features.

### Features / variables used

The dataset had a number of variables used as predictors for
predicting number of accommodations booked as the target variable.
These includes the following;

#### Predictor variables
__Number of sessions__ : This describes the number of sessions a customer made
on the booking site.

__City__ : This is the city from which a customer is accessing the booking site from

__Country__ : This is the country from which the user is accessing the booking site.
During the selection of various variables, you do not have the burden to decide this
as reference is automatically made from the city selected.

__Device Class__ : This is the type of device used to access the booking site. It has
the values desktop, phone or tablet

__Instant Booking__ : The is a feature on a booking site. Whether or not this
feature was used by a customer is included in predicting the number of day to
be booked

__User Verification Status__ : Whether or not a customer who visited the site
has been verified is included in predicting number of days to be booked.

### Target variable
__ Number of accommodation days to be booked__


### Tools and method used
Automated machine learning (AutoML) was employed to deliver a high
accuracy optimized prediction model. The model is used to create
an API that receives request, makes and send prediction as response
to this web application.

With the user interface provided here, various features describing customers
behaviours and attributes can be selected to make a prediction.

Among others, the tools used included the following

* TPOT as an AutoML package to develop the machine learning model
* Dash to build this web application as the User Interface
* Flask to develop the API for the machine learning model


### Project output

The main output of this project were the following

* Machine learning API deployed
* Machine learning web application


