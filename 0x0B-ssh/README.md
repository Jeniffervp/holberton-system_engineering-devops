# 0x0B. SSH

![N|Solid](https://blogs.encamina.com/por-una-nube-sostenible/wp-content/uploads/sites/19/2019/01/ssh_header-1024x534.jpg)

## Definition

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely. It provides a text-based interface by spawning a remote shell. After connecting, all commands you type in your local terminal are sent to the remote server and executed there.

In this cheat sheet-style guide, we will cover some common ways of connecting with SSH to achieve your objectives. This can be used as a quick reference when you need to know how to do connect to or configure your server in different ways.

### Tasks

`Madatory:`

| Name | Description |
|-----| -------|
| 0. Use a private key | Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/holberton` with the user `ubuntu`. |
| 1. Create an SSH key pair | Write a Bash script that creates an RSA key pair. |
| 2. Client configuration file | Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file. |
| 3. Let me in! | Now that you have successfully connected to your server, we would also like to join the party. |
| 4. Client configuration file (w/ Puppet) | Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password. |
