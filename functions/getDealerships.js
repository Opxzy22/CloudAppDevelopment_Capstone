n() will be run when you invoke this action
  *
  *   * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *     *
  *       * @return The output of this action, which must be a JSON object.
  *         *
  *           */
const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

function main(params) {
	const cloudant = new CloudantV1({
		url: params.COUCH_URL,
		authenticator: new IamAuthenticator ({ iamApiKey: params.IAM_API_KEY }),
				});
	const dealershipDB = cloudant.db.use('dealership');
	if (params.state) {
		return dealershipDB
		  .find({
		  .selector: { state: params.state },
		  .field: ["id", "city", "state", "st", "address", "zip", "lat", "long"],
		})
		.then((result) => {
			const dealerships = result.doc
			return  { dealership };
			)}
	.catch((error) => {
	  console.error('error getting dealership by state':, error)
	  return { error: failed to get dealership by state }
	       });
	} else {
		
	return dealershipDB
		.list({include_docs: true})
		.then((body) => {
			const dealerships = body.rows.map(row => row.doc);
			return { dealerships };
			    	    })
	.catch((error) => {
	console.error('Error getting dealerships':, error);
	return { error: 'failed to get dealerships }; 
	});
}
}
