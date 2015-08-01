var request = require('request');
var qs = require('querystring');

var url = 'https://yboss.yahooapis.com/geo/placespotter';

var params = qs.stringify({
    documentContent: 'I live in London',
    documentType: 'text/plain',
    outputType: 'json'
});


var key = 'dj0yJmk9UzhPZlRNbmFwQjdZJmQ9WVdrOWNXSlBRM2hOTm1VbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1lNw--'
var secret = '8eb66129a2d550779614eb358f3f6bfecac854ef'

var oauth = {
    consumer_key: key,
    consumer_secret: secret
};

request.get({ url: url + '?' + params, oauth: oauth, json: true }, function(e, r, body) {
          console.log(body);
          console.log(body.bossresponse.placespotter)
          for (item in body.placespotter.document) {
            console.log(item);
          }
});


