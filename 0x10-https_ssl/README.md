# 0x10-https_ssl

![N|Solid](https://negosentro.com/wp-content/uploads/2016/01/secure-webhosting1-1024x739.jpg)

### HTTPS and HTTP

Hyper Text Transfer Protocol Secure (HTTPS) is the secure version of HTTP, the protocol over which data is sent between your browser and the website that you are connected to. The 'S' at the end of HTTPS stands for 'Secure'. It means all communications between your browser and the website are encrypted. HTTPS is often used to protect highly confidential online transactions like online banking and online shopping order forms.

Web browsers such as Internet Explorer, Firefox and Chrome also display a padlock icon in the address bar to visually indicate that a HTTPS connection is in effect.

### Tasks
`Mandatory`

| NAME | DESCRIPTION |
| ------ | ------ |
| 0. HTTPS ABC | What is HTTPS?, Why do you need HTTPS?, You want to setup HTTPS on your website, where shall you place the certificate? |
| 1. World wide web | Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains. |
| 2. HAproxy SSL termination | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www. |
| 3. No loophole in your website traffic | A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS. |