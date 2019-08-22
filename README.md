# SwitchPointEncryption
A Proof of Concept for SwitchPoint Encryption. 

SwitchPoint Encryption is an Cryptographic Technique/System that is inspired by the idea of a "moving target" where in the integrity of sensitive data (particularly data that is subject to change often) is protected by means of merely "changing the Encryption mapping" from time to time. 

By doing the above, if the read-access of a database/datastore has been compromised, frequent updates of the "Encrypted" Sensitive Data creates a sense of ambiguity over the expiry/validity of a previously procured instance of the encrypted data. 
In simple words, the attacker is unsure if the "sensitive data" he/she is trying to steal has changed, or if it's just an updated CipherText. 

Another key feature of this design is that when moving from CipherText state to the next, it is never Decrypted at any intermidate step. Rather, the existing CipherText is Encrypted in a way where knowledge of the Timestamp at which it was Encrypted is enough to decrypt it back to its PlainText state. 


<h1> How to run this </h>

<h3> Prerequisities </h3>

* MongoDB
* Python3's MongoDB Client - pymongo

<h3> Setup </h3>

In your MongoDB, create a db named "db" and a collection named "users". 

<h3> Running </h3>

Firstly run the create_user file to insert a document into your collection to run SwitchPoint Encryption on. 

<code> python create_user.py </code>

Following that, update the settings file, and set the value of "username" to the username of the value you just inserted, and save.

Once that is done, you can start the SwitchPoint Engine by running the following:

<code> python server.py </code>

With the SwitchPoint Engine running, you can observe that your password's Encryption gets updated every 5 seconds. (can be altered in the settings.ini file)
You can verify at any point that despite the constant updates, a valid mapping still exists to your original password by opening a seperate terminal window and running the following:

<code> python verify.py </code>

The verification may be run while the SwitchPoint Engine is still running or if the instance has been killed off. At any point the Engine may be turned off and on (with or without an updated frequency) and it will pick up where it left off. 
