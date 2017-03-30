
module.exports = function(){

	var PORT = 33333
	var HOST = '127.0.0.1'

	var dgram = require('dgram')
	var message = new Buffer('Example message from client')

	var client = dgram.createSocket('udp4')
	client.send(message, 0, message.length, PORT, HOST, (err)=>{
		if (err) throw err
		console.log('UDP message sent to ' + HOST +':'+ PORT)
		client.close()
	})
}
