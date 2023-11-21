from typing import Dict
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests

def post_review(param_dict: Dict) -> Dict:
    """IBM Cloud Function that posts a review for a dealership

    Args:
        param_dict (Dict): Input parameter with COUCH_USERNAME, IAM_API_KEY, and review details

    Returns:
        Dict: Success message or an error message
    """
  try:
    client = cloudant.iam(
      account_name=param_dict["COUCH_USERNAME"],
      api_key=param_dict["IAM_API-KEY"],
      connect=True,
    )
    # Get the reviews database
    reviewDB = client['review']

    # Extract reviews details from the input parameters
    new_review = {
    "name": param_dict.get("name"),
    "dealership": param_dict.get("dealership"),
    "review": param_dict.get("review"),
    "purchase": param_dict.get("purchase"),
    "purchase_date": param_dict.get("purchase_date"),
    "car_make": param_dict.get("car_make"),
    "car_model": param_dict.get("car_model"),
    }

    # insert the new review into the review database
    response = reviewDB.create_document(new_review)

   # disconnect from cloudant
    client.disconnent()

    return {"message": "review created succesfully" "review_id": response["_id]"}

except Cloudant_exception as cloudant_exception:
    print("Unable to connect to Cloudant")
    return {"error": str(cloudant_exception)}
except (requests.exceptions.RequestException, ConnectionResetError) as err:
    print("Connection error")
    return {"error": str(err)}

    
   
  

    
