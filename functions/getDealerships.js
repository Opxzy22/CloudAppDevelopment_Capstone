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
	const cloudant = cloudant({
		url: params.COUCH_URL,
		plugins: { iamauth { iamApiKey: params.IAM_API_KEY } }
				});
	const dealershipDB = cloudant.db.use('dealership');
		
	return dealershipDB.list({include_docs: true})
		.then((body) => {
			const dealerships = body.rows.map(row => row.doc);
			return { dealerships };
			    	    })
	.catch((error) => {
		console.error('Error getting dealerships':, error)
		return { error: 'failed to get dealerships }; 
	});
}

