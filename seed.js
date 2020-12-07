var
    AWS = require("aws-sdk"),
    DDB = new AWS.DynamoDB({
        apiVersion: "2012-08-10",
        region: "us-east-1"
    }),
    DOG_DATA_ARR = require("./dog_data.json");

function addNewItemsFromJSON(){
	console.log("All items now removed, re-seeding now");
	var 
		dog = {},
		dog_formatted_arr = [],
		params = {};


	for(var i_int = 0; i_int < DOG_DATA_ARR.length; i_int += 1){
		dog = {
	    	PutRequest: {
	    		Item: {
	    			petname: {
	    				"S": DOG_DATA_ARR[i_int].petname_str
	    			},
	    			breed: {
	    				"S": DOG_DATA_ARR[i_int].breed_str
	    			},
	    			gender: {
	    				"S": DOG_DATA_ARR[i_int].gender_str
	    			},
	    			data_found: {
	    				"S": DOG_DATA_ARR[i_int].date_found_str
	    			},
	    			notable_features: {
	    				"S": DOG_DATA_ARR[i_int].notable_features_str
	    			}
	    		}
	    	}
	    };
	    dog_formatted_arr.push(dog);
	}
	params = {
		RequestItems: {
			"lostcats": dog_formatted_arr.reverse()
		}
	};
	DDB.batchWriteItem(params, function(err, data){   
		if(err){
			throw err;
		}
		console.log("OK");         
	});
}

(function init(){
	addNewItemsFromJSON();
})();
