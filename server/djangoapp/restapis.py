import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
def get_request(url, **kwargs):
  print(kwargs)
  print("GET from: {} " .format(url))

  try:
    response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', IAM_API_KEY))
    
  except:
    # If any error occurs
    print("Network exception error")
    status_code = response.status_code
    print("with status {} " .format(status_code))
    json_data = json.load(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, params=kwargs, json=payload):
  response = request.post(url, params=kwargs, json=payload)
  return response 


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
  results = []
  # Call get_request with a URL parameter
  json_data = get_request(url)

  if json_data:
    # Get the row list in JSON as dealers
    dealers = json_data["rows"]

     # For each dealer object
    for dealer in dealers:
      # Get its content in `doc` object
      dealer_doc = dealer["doc"]
      # Create a CarDealer object with values in `doc` object
      dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
      results.append(dealer_obj)
  return results

def get_dealers_by_state(url, state, **kwargs):
  results = []
  json_data = get_request(url, state=state)
  results.append(json_data)
  return results
      
    


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
from django.http import HttpResponse

def get_dealer_reviews_from_cf(url, dealerId=dealer_id):
    results = []

    # Call get_request() with specified arguments
    json_data = get_request(url, dealerId=id)

    if json_data:
        reviews_row = json_data.get("rows", [])

        for review in reviews_row:
            reviews_doc = review.get("doc", {})

            # Parse JSON results into a DealerReview object list
            reviews_obj = DealerReview(
                id=reviews_doc.get("id", ""),
                name=reviews_doc.get("name", ""),
                dealership=reviews_doc.get("dealership", ""),
                review=reviews_doc.get("review", ""),
                purchase=reviews_doc.get("purchase", ""),
                purchase_date=reviews_doc.get("purchase_date", ""),
                car_make=reviews_doc.get("car_make", ""),
                car_model=reviews_doc.get("car_model", ""),
                car_year=reviews_doc.get("car_year", "")
            )

            # Call the function to analyze sentiment and add it to the review object
            review_obj.sentiment = analyze_review_sentiments(reviews_obj.review)

            results.append(reviews_obj)

        return HttpResponse(results)

    else:
        return HttpResponse("Error: Unable to fetch data from Cloud Foundry.")



# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse

def analyze_review_sentiments(text, **kwargs):
    # Call get_request() with specified arguments

    analyzed_reviews = []

    # Prepare parameters for the Watson NLU API request
    params = {
        "text": kwargs.get("text", ""),
        "version": kwargs.get("version", ""),
        "features": kwargs.get("features", ""),
        "return_analyzed_text": kwargs.get("return_analyzed_text", "")
    }

    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/f6a43d38-3b00-4b44-b613-5b9b24ed7d6d"
    # Make a GET request to the Watson NLU service
    response = requests.get(
        url,
        params=params,
        headers={'Content-Type': 'application/json'},
        auth=HTTPBasicAuth('apikey', 'IAM_API_KEY')
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Get the returned sentiment label such as Positive or Negative
        # Extract sentiment score
        sentiment_score = response.json().get('sentiment', {}).get('document', {}).get('score', None)

        # Add sentiment score to the review data
        analyzed_review = {
            'content': text,
            'sentiment_score': sentiment_score
        }

        analyzed_reviews.append(analyzed_review)

        # You can now use 'analyzed_reviews' as needed, for example, return it as JSON
        return HttpResponse(analyzed_reviews)

    # Handle errors if the request was not successful
    else:
        return HttpResponse(f"Error: {response.status_code}")




