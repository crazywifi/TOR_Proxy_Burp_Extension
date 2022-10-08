# TOR_Proxy_Burp_Extension
## Enable TOR Proxy By Burp...Make yourself Anonymous...

### Uses:
You can now enable the TOR proxy directly from Burp and use it in Browser.

### Steps: 
Download TOR Binary https://www.torproject.org/download/tor/ </br>
Install the Burp extension.</br>
In Burp extension provides the path of the downloaded TOR binary.</br>
Use On for starting the TOR proxy and Off for shutting down the TOR proxy.</br>
Now when the TOR proxy is On, navigate to "User Options" in the Burp and scroll down to "SOCKS Proxy".</br>
Check the "Use SOCKS Proxy" and add</br>
SOCKS proxy host: 127.0.0.1</br>
SOCKS proxy port: 9050</br>
Now all your traffic goes to Burp and from Burp it goes to TOR.</br>
When you click on the Off button, uncheck the "Use SOCKS proxy".</br>

### Read More:
https://lazyhacker22.blogspot.com/2022/08/TORProxyBurpExtension.html
</br>

</br>
</br>
</br>
</br>

![Alt Text](https://raw.githubusercontent.com/crazywifi/TOR_Proxy_Burp_Extension/main/TOR_Proxy_Burp_Extesnion.gif)
