
<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="150" src="https://github.com/conwnet/shadowsocks-kodi/raw/master/resources/icon.png" alt="Shadowsocks Kodi logo"></a></p>


<h3 align="center">
    Run Shadowsocks on Kodi!
</h3>

## Get Started

You can download the latest version from [Github Releases](https://github.com/conwnet/shadowsocks-kodi/releases)

1. Install the addon on your kodi.
2. Configure your Shadowsocks.
3. Restart services to take effect.

Then set the SOCKS5 proxy in your Kodi System Settings.

**Settings -> System -> Internet access**

- Use proxy server -> **true**
- Proxy type -> **SOCKS5** (or **SOCKS5 with remmote DNS resolving**)
- Server -> *the_value_you_set* (default **127.0.0.1**)
- Port -> *the_value_you_set* (default **1080**)

> I had a few hazy memories, the Proxy type **SOCKS5** maybe not work on some previous version of Kodi or LibreELEC (but I test it works at LibreELEC 9.2.1 now). If you have this problem, please try to upgrade your Kodi or convert the SOCKS5 proxy to a HTTP proxy use some softwares such as **polipo**.

## Check up

You can login your kodi with ssh and display the ports usage.

As shown below, we can see our Shadowsocks services running at PID 653.

```
LibreELEC:~ # netstat -lntp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
...
tcp        0      0 127.0.0.1:1080          0.0.0.0:*               LISTEN      653/kodi.bin
...
```

You can test whether your services work as your expected use `curl`.

```
LibreELEC:~ # curl -x socks5://127.0.0.1:1080 ifconfig.io/ip
```

## Screenshots

![Shadowsocks kodi](./resources/screenshot-01.png)
