# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# write a route for post request
@app.route('/emo')
def review():

    # extract the customer_review by writing the appropriate 'key' from the JSON data
    review = request.json.get('key')

    # check if the customer_review is empty, return error
    if not review:

        return jsonify({'status' : 'error' , 
                        'message' : 'Empty response'})

    # if review is not empty, pass it through the 'predict' function.
    # predict function returns 2 things : sentiment and path of image in static folder
    # example : Positive , ./static/assets/emoticons/positive.png

    else:

        sen , imgp = sa.predict(review)

        return jsonify({'data':{'emotion':sen,'image':imgp} , 'success':'success'})


if __name__  ==  "__main__":
    app.run(debug = True)