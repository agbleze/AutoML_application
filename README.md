## BookingGauger: Automated Machine Learning API for predicting number of accommodation days an online visitor will book.

## Overview

This project builds a data processing pipeline and modeling with Automated Machine Learning (AutoML) to request prediction of number of days to be booked for accommodation by a user. 

## Project description

The aim of this project is to predict the number of days that
customers are likely to book a room for an accommodation based on user bahaviour.
The end-user is an accommodation provider who sought to obtain
an intelligent tool that can enable the prediction of number of days that an online vistor will book a room for accommodation based on a number of features.

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
an [API](https://github.com/agbleze/booking_days_predictor_api.git) that receives request, makes and send prediction as response to an [app](https://github.com/agbleze/booking_gauger_ui.git).


### Project output
A reusable package that is truely plug and play.

### How to install 

1. Create a virtual environment (replace 'project' with your prefreed pathname)

```python3 -m venv project_env```
 

2. Activate your virtual environment as follows

```source project_env/bin/activate```

3. Clone repository into the virtual environment created
With **_git already installed_**, run the command below in your terminal to get the code into your local environment

```git clone https://github.com/agbleze/AutoML_application.git```

Make sure you are in the directory of the cloned repo, now you can install the package

```pip install . ```


