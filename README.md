Description

SSH Tunnel through proxy requiring authentication

For Debian/Ubuntu/Mint

First install this Debian/Ubuntu/Mint package:

apt-get install connect-proxy

Export credentials if you are working behind proxy with authentication:

export HTTP_PROXY_USER=<user>

export HTTP_PROXY_PASSWORD=<password>

Access ssh config file on /etc/ssh/ssh_config and set remote host port:

Port 443

Set server alive interval for avoid connection lose:

ServerAliveInterval 20

Set ProxyCommand to use the connect recently installed package:

ProxyCommand connect -H <proxy>:<port> %h %p

Close ssh config file, then you are ready to execute ssh connection:

ssh -N -D localhost:1080 <remoteuser>@<remotehost>

Open Firefox, configure Connection settings to only use Socket 5 with:

Host: localhost Port: 1080

Enable also Proxy DNS when using SOCKS v5

Finally in Firefox search tab write the following:

about:config

Find network.proxy.allow_hijacking_localhost and set to true

Now you are ready to connect behind proxy and use Firefox to explore behind created tunnel
