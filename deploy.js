
var etherStickContract = web3.eth.contract(compiled.info.abiDefinition);

var etherStick = etherStickContract.new({from:web3.eth.accounts[0], data: compiled.code, gas: 300000}, function(e, contract){
    if(!e) {
      if(!contract.address) {
        console.log("Contract transaction send: TransactionHash: " + contract.transactionHash + " waiting to be mined...");

      } else {
        console.log("Contract mined! Address: " + contract.address);
        console.log(contract);
      }

    } else {
        console.log(e);
    }
})
