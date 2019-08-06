# 0x0A Configuration management

![N|Solid](https://www.hightechinstitute.nl/files/images/system/conf1webgr_800.jpg)

## Definition

Configuration Management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

Automation plays an essential role in server configuration management. It's the mechanism used to make the server reach a desirable state, previously defined by provisioning scripts using a tool's specific language and features. Automation is, in fact, the heart of configuration management for servers, and that's why it's common to also refer to configuration management tools as Automation Tools or IT Automation Tools.

### Tasks

`Madatory:`

| Name | Description |
|-----| -------|
| 0. Create a file | Using Puppet, create a file in `/tmp`. Requirements: File path is `/tmp/holberton`. File permission is `0744`. File owner is `www-data`. File group is `www-data`. File contains `I love Puppet`. |
| 1. Install a package | Using Puppet, install `puppet-lint`. Requirements: Install `puppet-lint`. Version must be `2.1.1` |
| 2. Execute a command | Using Puppet, create a manifest that kills a process named `killmenow`. Requirements: Must use the `exec` Puppet resource. Must use `pkill`. |
