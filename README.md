# A revolutionary way to farm crops.
A machine learning model for crop recommendation.

https://youtu.be/nAfO0CTmQ1s

https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/256/918/datas/original.png![image](https://user-images.githubusercontent.com/26531244/196326958-b266d75f-26bd-4a06-bbfc-94fbeedef083.png)

https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/256/919/datas/original.png![image](https://user-images.githubusercontent.com/26531244/196326991-9ead6b4c-7391-4b4f-ab64-43716633f747.png)

Developed during hackTX 2022.

To run the app:

- download al the files and keep the same folder structure.
- in your terminal, go to the folder that contains these files
- run `export FLASK_APP=my_first_flask.py`
- run `flask run`
- copy the URL that is printed in the terminal, and paste it into a browser

## Inspiration

Recently, there has been a trend of lower agricultural engagement: lower employment over time (here) combined with increasing urbanization and a changing climate has led to stress on food production and farmers' livelihoods. Its in this way, we want to help farmers maximize the efficiency of their land use, allowing food production to be continued more sustainably in a changing, challenging future.

https://res.cloudinary.com/devpost/image/fetch/s--B5qQON2b--/c_limit,f_auto,fl_lossy,q_auto:eco,w_900/https://ourworldindata.org/exports/cropland-use-over-the-long-term_v6_850x600.svg![image](https://user-images.githubusercontent.com/26531244/196326896-80c36908-1104-4f9e-8c2e-072fd0abdbc7.png)


## What it does

## Farmers can input baseline indicators of their soil quality--ratio of nitrogen, phosphorous, potassium, pH--as well as their regional temperature, humidity, and average rainfall. Then, farmers receive a recommendation for a crop type most suitable to maximize productivity and profitability for the farmer.

## How we built it

We primarily utilized a K-nearest-neighbor model as the machine learning algorithm to learn from our training data. For the web-application, we used HTML and CSS as well as Flask to create our tool.

## Challenges we ran into

Initially, we experienced a lot of trouble identifying the right dataset to fit our problem scope. On the World In Data (website), there were many potential datasets, but they failed to provide us with the right input variables or were very hard to use. In the end, we used Crop Recommendation Dataset on Kaggle.

Another issue we ran into was connecting the front end and back end (a.k.a. transmitting inputs from the user to python script and getting the return value to the web app). However, this challenge was also where our group learned the most, and we eventually implemented a full-stack design.

## Accomplishments that we're proud of

We have 97.7% accuracy for our KNN model (validated for the testing data split).

## What we learned

- Front end and full-stack implementation
- Strengths and weaknesses of several machine learning algorithms
- Evaluating the quality of different datasets

## What's next for FarmML

We plan on branching out to a more diverse selection of crops and using region-specific crop data/availability of crops to farmers for a more customized recommendation.

We could also factor in the sustainability of each crop to the environment, or recommend sustainable farm practices such as crop rotation for predicting crop types in concurrent years.

## Built With

css
flask
html5
javascript
keras
machine-learning
python
tensorflow
