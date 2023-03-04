from setuptools import setup



setup(name='booking_gauger_tpoter',
      version='0.0.1',
      author='Agbleze Linus',
      packages=['booking_gauger_tpoter'],
      description='This package trains and develop machine learning model \
                  for predicting number of days a room will be booked for accommodation \
                 by an online visitor. The package uses AutoML under the hood to train \
                and select best algorithm for the prediction.',
    zip_safe=False,
    license='MIT'
    )