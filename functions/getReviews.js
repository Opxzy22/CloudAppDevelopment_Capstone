const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

function main(params) {
  const cloudant = new CloudantV1 ({
    authenticator: new Authenticator({ apikey: params.IAM_API_KEY }),
    url: params.COUCH_URL,
  });

  const reviewDB = cloudant.db.use('review')
  if (params.dealerId) {
    return reviewDB
      .find({
        .selector: { dealership: params.id },
        .field: ["id", "name", "dealership", "review", "purchase", "purchase_date", "car_make", "car_model", "car_year"],
            })
    .then((result) => {
      const review = result.docs
      return { review };
    })
    .catch((error) => {
      console.error("Error getting review by dealerId, error);
      return { "failed to get review by dealerId" }
    });
  } else {
    return promise.resolve({error: missing dealerId parameters});
  }
}
  
    
    
