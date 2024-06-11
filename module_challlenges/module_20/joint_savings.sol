/*
Joint Savings Account
---------------------

To automate the creation of joint savings accounts, you will create a solidity smart contract that accepts two user addresses that are then able to control a joint savings account. 
Your smart contract will use ether management functions to implement various requirements from the financial institution to provide the features of the joint savings account.

The Starting file provided for this challenge contains a `pragma` for solidity version `5.0.0`.
You will do the following:

1. Create and work within a local blockchain development environment using the JavaScript VM provided by the Remix IDE.

2. Script and deploy a **JointSavings** smart contract.

3. Interact with your deployed smart contract to transfer and withdraw funds.

*/

pragma solidity ^0.5.0;

// Define a new contract named `JointSavings`
contract JointSavings {

    /*
    Inside the new contract define the following variables:
    - Two variables of type `address payable` named `accountOne` and `accountTwo`
    - A variable of type `address public` named `lastToWithdraw`
    - Two variables of type `uint public` named `lastWithdrawAmount` and `contractBalance`.
    - Comment: Address stores metamask public keys that are used to withdraw or deposit funds: 0x4B12968BcF76d9C67aF708a456d18F09D3733D91
    - Comment: Address also stores smart contract address, a unique hash address when you deploy a contract on a blockchain: 0xf8e81D47203A594245E36C48e151709F0C19fBe8
    - Comment: Payable can receive Ethers, address public is storing address, unit public are amounts
    
    */
    address payable accountOne; 
    address payable accountTwo;
    address public lastToWithdraw;
    uint public lastWithdrawAmount;
    uint public contractBalance;

    /*
    Define a function named **withdraw** that will accept two arguments.
    - A `uint` variable named `amount`
    - A `payable address` named `recipient`
    */
    function withdraw(uint amount, address payable recipient) public {

        /*
        Define a `require` statement that checks if the `recipient` is equal to either `accountOne` or `accountTwo`. The `requiere` statement returns the text `"You don't own this account!"` if it does not.
        */
        // YOUR CODE HERE!
        // Comment: Can't withdraw unless you are accountOne or AccountTwo
        require(recipient == accountOne || recipient == accountTwo, "You don't own this account!");

        /*
        Define a `require` statement that checks if the `balance` is sufficient to accomplish the withdraw operation. If there are insufficient funds, the text `Insufficient funds!` is returned.
        */
        // YOUR CODE HERE!
        // Comment: If balance of smart contract is less than amount being withdrawn, can't do it
        require(address(this).balance > amount, "Insufficient funds!");

        /*
        Add and `if` statement to check if the `lastToWithdraw` is not equal to (`!=`) to `recipient` If `lastToWithdraw` is not equal, then set it to the current value of `recipient`.
        */
        // YOUR CODE HERE!
        // Comment: If recpient is not lastToWithdraw, then make this recipient the lastToWithdraw
        if(lastToWithdraw != recipient){
            lastToWithdraw = recipient;
        }

        // Call the `transfer` function of the `recipient` and pass it the `amount` to transfer as an argument.
        // YOUR CODE HERE!
        // Comment: transferring amount withdrawn to recipient
        recipient.transfer(amount);

        // Set  `lastWithdrawAmount` equal to `amount`
        // YOUR CODE HERE!
        // Comment: setting lastWithdrawAmount to this new amount being withdrawn
        lastWithdrawAmount = amount;

        // Call the `contractBalance` variable and set it equal to the balance of the contract by using `address(this).balance` to reflect the new balance of the contract.
        // YOUR CODE HERE!
        // Comment: Updating current balance of smart contract
        contractBalance = address(this).balance;
    }

    // Define a `public payable` function named `deposit`.
    function deposit() public payable {

        /*
        Call the `contractBalance` variable and set it equal to the balance of the contract by using `address(this).balance`.
        */
        // YOUR CODE HERE! 
        // Commment: Updating balance when depositing funds. "Payable" means function can receive Ethers
        contractBalance = address(this).balance;
    }

    /*
    Define a `public` function named `setAccounts` that receive two `address payable` arguments named `account1` and `account2`.
    */
    function setAccounts(address payable account1, address payable account2) public{

        // Set the values of `accountOne` and `accountTwo` to `account1` and `account2` respectively.
        // YOUR CODE HERE!
        // Comment: Assigning public keys to accountOne and AccountTwo
        // Comment: Remix VM (Cancun) gives 10 accounts for testing, two of which will be used here
        accountOne = account1;
        accountTwo = account2;
    }

    /*
    Finally, add the **default fallback function** so that your contract can store Ether sent from outside the deposit function.
    */
    // YOUR CODE HERE!
    // Commment: Enables smart contract to receive Ethers
    function() external payable { }
}

// Deployment Comments
// 1. Enter 0 in Value, and press Deploy to deploy the smart contract
// 2. Enter conversion of 1 Ether to Wei in Value, and click "Deposit" in Joint Savings Smart Contract
// 2. Account balance will show 1 less Ether plus gas price of transaction
// 3. Enter conversion of 10 Ether to Wei in Value, and click "Deposit" in Joint Savings Smart Contract
// 4. Enter 5 Ether, and click "Deposit" in Joint Savings Smart Contract
// 5. Copy next two addresses from top into account 1 & 2 in SetAccounts (smart contract). Click "Transact"
// 5. Withdraw 5 ether into accountOne and 10 ether into accountTwo. 
// 5. After each transaction, use the contractBalance function to verify that the funds were withdrawn from your contract. 
// 5. Also, use the lastToWithdraw and lastWithdrawAmount functions to verify that the address and amount were correct.