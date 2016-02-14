// To compile the serpent file, run
// serpent mk_contract_info_decl contract.se
var exec = require('child_process').exec;
exec('serpent mk_contract_info_decl ether-on-a-stick/contract.se',
    function (error, stdout, stderr) {
        if (error !== null) {
             console.log('exec error: ' + error);
        }
        var compiledContract = JSON.parse(stdout);
        // console.log('stdout: ' + stdout);
        // console.log('stderr: ' + stderr);

        var etherStickContract = web3.eth.contract(compiledContract.info.abiDefinition);

        var etherStick = etherStickContract.new({from:web3.eth.accounts[0], data: compiledContract.code, gas: 300000}, function(e, contract){
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

    });

