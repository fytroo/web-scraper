var argv = require('argv')

argv.option({
  name: 'query',
  short: 'q',
  type: 'string',
  description: 'query keyword',
  example: '-q banana'
})

argv.option({
  name: 'number',
  short: 'n',
  type: 'int',
  description: 'number of images',
  example: '-n 10'
})

var Scraper = require ('images-scraper')
  , bing = new Scraper.Bing();

bing.list({
	keyword: argv.run().options.query,
	num: argv.run().options.number,
	detail: true
})
.then(function (res) {
	console.log(JSON.stringify(res));
}).catch(function(err) {
	console.log('err',err);
})
