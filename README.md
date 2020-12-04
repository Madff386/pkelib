# PKElib
Library for public key encryption, use `var = pke(message)` to create a pke object.  
Then you can use the `var.encrypt()` and `var.decrypt()` methods to encrypt and decrypt the message.  
By deafault they will encyrpt and decrypt with default keys, to do it with different keys just pass them to the `var.encrypt()` and `var.decrypt()` methods.  
eg:  
 - `var.encrypt(encrypt_key, main_key)`   
 - `var.decrypt(decrypt_key, main_key)`
