## Setup
Use these scripts to set up your web servers.
Clone this repository into the web-01 and web-02 servers or copy the scripts into respective files.
run the scripts on web-01 and web-02.

### setup
1. Install MySQL 5.7x   
```./mysql_install mysql_signature_key```  


2. Append alx-ssh public key into web-01 and web-02 authorized_keys file   
```sudo ./append_key alx-ssh_key.pub```  

