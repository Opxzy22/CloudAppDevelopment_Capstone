import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
def get_request(url, **kwargs):
  print(kwargs)
  print("GET from: {} " .format(url))

  try:
    response = requests.get(url, params=kwargs, headers={'Content-Type': 'application/json'})
    
  except:
    # If any error occurs
    print("Network exception error")
    status_code = response.status_code
    print("with status {} " .format(status_code))
    json_data = json.load(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


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
def get_dealer_reviews_from_cf(url, dealerId=dealer_id):
  results = []
# - Call get_request() with specified arguments
  json_data = get_request(url, dealerId=id)

  if json_data:
    reviews_row = json_data("rows")

    for review in reviews_row:
      reviews_doc = review("doc")
# - Parse JSON results into a DealerView object list
      reviews_obj = DealerReview(id=reviews_doc["id"], name=reviews_doc["name"], dealership=reviews_doc["dealership"],
                                 review=reviews_doc["review"], purchase=reviews_doc["purchase"], purchase_date=reviews_doc["purchase_date"],
                                 car_make=reviews_doc["car_make"], car_model=reviews_doc["car_model"] car_year=reviews_doc["car_year"])
      results.append(reviews_obj)

  return HttpResponse(results)


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



