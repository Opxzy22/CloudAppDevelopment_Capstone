// Import necessary libraries
const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

// Main function that serves as the entry point for the IBM Cloud Function
function main(params) {
  // Create a Cloudant client instance
  const cloudant = new CloudantV1({
    url: params.COUCH_URL,
    authenticator: new IamAuthenticator({ iamApiKey: params.IAM_API_KEY }),
  });

  // Get a reference to the 'dealership' database
  const dealershipDB = cloudant.db.use('dealership');

  // Check if the 'state' parameter is provided in the input parameters
  if (params.state) {
    // If 'state' is provided, filter dealerships by state using Cloudant's find method
    return dealershipDB
      .find({
        selector: { state: params.state },
        fields: ["id", "city", "state", "st", "address", "zip", "lat", "long"],
      })
      .then((result) => {
        // Extract the found dealership document
        const dealerships = result.docs;
        return { dealerships };
      })
      .catch((error) => {
        // Handle errors during the find operation
        console.error('Error getting dealership by state:', error);
        return { error: 'Failed to get dealership by state' };
      });
  } else {
    // If 'state' is not provided, list all dealerships using Cloudant's list method
    return dealershipDB
      .list({ include_docs: true })
      .then((body) => {
        // Extract the list of dealerships from the result
        const dealerships = body.rows.map(row => row.doc);
        return { dealerships };
      })
      .catch((error) => {
        // Handle errors during the list operation
        console.error('Error getting dealerships:', error);
        return { error: 'Failed to get dealerships' };
      });
  }
}
