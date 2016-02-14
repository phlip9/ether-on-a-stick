contract mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function mortal() {
      owner = msg.sender;
    }

    /* Function to recover the funds on the contract */
    function kill() {
      if (msg.sender == owner)
        suicide(owner);
    }
}

contract greeter is mortal {
    /* define variable greeting of the type string */
    string greeting;

    /* this runs when the contract is executed */
    function greeter(string _greeting) public {
        greeting = _greeting;
    }

    /* main function */
    function greet() constant returns (string) {
        return greeting;
    }
}

------

"contract mortal { /* Define variable owner of the type address*/ address owner; /* this function is executed at initialization and sets the owner of the contract */ function mortal() { owner = msg.sender; } /* Function to recover the funds on the contract */ function kill() { if (msg.sender == owner) suicide(owner); } } contract greeter is mortal { /* define variable greeting of the type string */ string greeting; /* this runs when the contract is executed */ function greeter(string _greeting) public { greeting = _greeting; } /* main function */ function greet() constant returns (string) { return greeting; } }"

greeter.address = "0x73b21660a442de2ce1012695f7daf2d9d110e615"

greeter.kill.sendTransaction({ from: philip })

------

var greeter = greeter_contract.new(
  _greeting,
  {
    from: philip,
    data: greeter_compiled.greeter.code,
    gas: 1000000
  }, function(e, contract){
    if(!e) {
      if(!contract.address) {
        console.log("Contract transaction send: TransactionHash: " + contract.transactionHash + " waiting to be mined...");
      } else {
        console.log("Contract mined! Address: " + contract.address);
        console.log(contract);
      }
    }
  })
