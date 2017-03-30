
module.exports = function(){

	var PORT = 4173
	var HOST = '127.0.0.1'

	var dgram = require('dgram')
	var server = dgram.createSocket('udp4')

	server.on('listening', ()=>{
		let address = server.address()
		console.log('UDP Server listening on ' + address.address + ':' + address.port)
	})

	server.on('message', (message, remote)=>{
		console.log(remote.address + ':' + remote.port +' - ' + message)
	})

	server.bind(PORT, HOST)

}
