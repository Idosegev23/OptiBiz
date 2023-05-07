from flask import Flask, request, jsonify
import tensorflow as tf
from optibiz_data_preprocessing import preprocess_data
from optibiz_recommendation_engine import train_recommendation_engine


# Load the trained model
# model = train_recommendation_engine(x_train, y_train, x_test, y_test, num_features, num_classes)

# Define the Flask app
app = Flask(__name__)


# Define the API endpoint for recommendations
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    # Get the input data from the request
    data = request.get_json()

    # Preprocess the data
    data = preprocess_data(data)

    # Make a prediction with the model
    prediction = model.predict(data)

    # Return the prediction as JSON
    return jsonify(prediction.tolist())


# Run the Flask app
if __name__ == '__main__':
    app.run()