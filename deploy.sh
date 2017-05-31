
IP="fc01::101"



if [ "$1" = "keys" ]; then
    cat ~/.ssh/id_rsa.pub | ssh pi@$IP "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"
fi


if [ "$1" = "code" ]; then

    ssh -6 pi@$IP 'rm -rf ~/rv-project && mkdir rv-project'

    scp -r [!.]* pi@\[$IP\]:rv-project/

fi