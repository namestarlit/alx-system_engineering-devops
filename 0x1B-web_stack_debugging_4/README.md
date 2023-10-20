## 0x1B. Web stack debugging #4
This is about debbuging nginx web server by increasing the limit of file   
descriptors (`ulimit`)  

Tested using apache beachmark: `ab -c 100 -n 2000 localhost/`
