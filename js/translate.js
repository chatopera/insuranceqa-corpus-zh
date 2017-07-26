var translate = require('@google-cloud/translate');

//var gcloud = require('google-cloud')({
//  projectId: "chatbot-mvp",
//  // For any APIs that accept an API key: 
//  key: 'AIzaSyB9DP8MmHdlZAjVkaWysaZ_tirb7KFxWH0'
//});

if(!process.env['GCLOUD_PROJECT_ID']){
    throw new Error("Can not find GCLOUD_PROJECT_ID in env.")
}

var GCLOUD_PROJECT_ID=process.env['GCLOUD_PROJECT_ID']
var GCLOUD_KEY=process.env['GCLOUD_KEY']

var translateClient = translate({
  projectId: GCLOUD_PROJECT_ID,
  key: GCLOUD_KEY
});

text = "It ultimately depends on what prescription drug plan you have. Not all drug plans are the same. The list of covered drugs (also known as a formulary for Medicare programs) will tell you whether your Cialis prescription will be covered. If it's listed as a covered drug, then you would only pay your share of the expense (deductible, copay, and/or coinsurance, etc.). If it's not a covered drug, then you would be responsible for 100% of the cost. It may simply be that the prescription drug plan you have does not cover this specific drug.\ At age 71, I'm assuming you're on Medicare. If so, regardless of whether your drug coverage is under a Medicare Advantage plan or through a stand-alone Part D plan, you would not be able to make any changes to your drug coverage until the annual enrollment period (October 15 - December 7 of each year). During the annual enrollment period, you can evaluate your options to see which carrier's plan will cover this prescription. If you're covered under an employer plan, options may be limited, but if more than one option is available, I would recommend reviewing each of them to see which plan will be most suitable for your needs. If it's an individual poilcy, I recommend contacting the agent who placed the covered for you (that person would be the servicing agent for the program) or call your insurance carrier directly to find out if it should be a covered drug under your plan. If you have a group policy, then you would need to either contact the carrier directly or your human resources department should be able to put you in contact with the appropriate person. I hope the information is helpful - please let me know if I can be of further assistance. Thanks very much."


function t(text, to='zh-CN'){
    return new Promise((resolve, reject)=>{
        // Translate a string of text. 
        translateClient.translate(text, to, function(err, translation) {
            if (!err) {
                resolve(translation)
            } else {
                reject(err)
            }
        });
    })
}

// test
// t(text).then((result)=>{
//     console.log("result", result)
// }, (err)=>{
//     console.log("err", err)
// })
exports  = module.exports = t;
