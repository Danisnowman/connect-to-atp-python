# connect to atp using docker and python
Datos 1 

# Change this in the ora file
`WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="/wallet")))SSL_SERVER_DN_MATCH=yes`

# Build the image 
`docker build --no-cache --force-rm=true -t atpython .`

# Run it 


    docker run \
    -e DB_USER=$user \
    -e DB_PASSWORD=$pass \
    -e DB_CONNECTIONSTRING=$CONNECTIONSTRING \
    atpython


# With ATP 

    docker run -it -p 3000:3000 -v /home/ubuntu/Datos_1/wallet:/wallet -e DB_USER=$DB_USER -e DB_PASSWORD=$DB_PASS -e DB_CONNECTIONSTRING=$CONNECTIONSTRING -e TNS_ADMIN=/wallet atpython


# With PostgreSQL AWS RDS