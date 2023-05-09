# End-Point-Ransomware-Detection-and-Mediation

The project discusses various aspects of cyber attacks, particularly phishing and reverse shell attacks, and how they can be carried out. Phishing is a type of attack where the perpetrator poses as a trustworthy organization to trick the victim into revealing sensitive data. The attacker typically uses email, text message, or instant message that appears to be from a reputable source like a bank or social media platform. The attacker creates a sense of urgency or curiosity to entice the victim to click on a link that leads to a fake website where the victim is prompted to enter their login credentials or other sensitive information.

Then details how to set up a mail server for a phishing attack using the Kamatera cloud platform. The process involves purchasing and configuring a domain, installing the Kamatera Cloud Platform, installing iRedMail, configuring the SMTP server, setting up outgoing email routing, implementing security measures like TLS encryption and firewall rules, and configuring mail policies to manage email accounts better.

Setting Up a Mail Server for Phishing attack – 
On the Kamatera cloud platform, an SMTP mail server was configured for the "zero.xyz" domain. The actions were as follows:

* Step 1: Purchasing and configuring a domain
The 'zero.xyz' domain was first ordered from Namecheap, and the DNS records were set up to direct visitors to our mail server.

* Step 2: Installing the Kamatera Cloud Platform
On the Kamatera cloud computing platform, we made an account and set up a server with the following settings: ‘zero.xyz' as the hostname, 2A CPU, 4096MB of memory, and a 20GB disk 1 are all specifications for the Ubuntu 20.04.5 LTS operating system.

* Step 3: Install iRedMail
We downloaded the installation script from the iRedMail website and ran it with sudo rights on our freshly installed Ubuntu Server 20.04.1.

* Step 4: Configuring iRedMail
After the installation, we went to http:// 83.225.9.90/iredadmin to the iRedMail web interface and configured our email domain and administrator account.

* Step 5: Configuring the SMTP Server
Next, we set up DNS records like MX records, configured firewall rules to permit incoming traffic to the server, and checked that the SMTP server was listening on the appropriate ports to configure the SMTP server to accept incoming emails from the internet.

* Step 6: Configure Outgoing Email Routing
Then, in order to prevent our outgoing emails from being marked as spam, we set up SPF and DKIM records on the SMTP server, configured the routing and relaying settings, and configured the SMTP server to route outgoing emails to their intended recipients.

* Step 7: Implementing Security Measures
We set up security measures like firewall rules and TLS encryption to prevent the server from being accessed by unauthorized users and to guarantee the privacy of email communication. For these uses, we employed the Let's Encrypt SSL/TLS certificates and the Ubuntu UFW firewall.

* Step 8: Configuring Mail Policies
To better manage our email accounts and lower the amount of spam or unwanted email that our users receive, we used iRedMail to set up mail policies like spam filters, email forwarding, and mailbox quotas.

* Step 9: Testing the server
For the purpose of identifying and troubleshooting any configuration issues that might be keeping our server from operating properly, we tested the server by sending and receiving emails to and from other email addresses.

The Project also discusses reverse shell attacks, where the attacker gains access to the victim's computer system and sends commands to it from a distance. In this attack, a backdoor is built on the victim's computer system by the attacker, who then uses it to connect to a remote server. The article then explains how to perform a reverse shell attack using Python programming language.



Finally, the project talks about generating keys using the RSA algorithm, which is one of the most commonly used public-key cryptographic algorithms. The RSA algorithm is based on the mathematical tenet that it is simple to multiply two large prime numbers together, but very difficult to factor the product back into its original primes. The article explains how the algorithm is more secure the larger the key size, and it is more challenging for an attacker to factorize the keys. The article concludes that cryptography is a critical tool in ensuring secure data transmission and must be implemented correctly to protect sensitive information from cyber attacks.

Generating Keys using `Rsa` Algorithm

```bash
python3 generate_keys.py
```

Encrypting the files

``` bash
python3 encrypt_file.py
```

Decrypting the file

```bash
python3 decrypt_file.py
```

With this the attack is complete
