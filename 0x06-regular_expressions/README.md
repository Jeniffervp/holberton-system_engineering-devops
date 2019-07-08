# 0x06. Regular expression

![N|Solid](https://i.imgur.com/EtpU3ss.jpg)

### Description

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the `//`:

`#!/usr/bin/env ruby`
`puts ARGV[0].scan(/127.0.0.[0-9]/).join`

### Tasks

`Madatory:`

| Name | Description |
| ------ | ------ |
| 0. Simply matching Holberton | Requirements:-The regular expression must match Holberton. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method |
| 1. Repetition Token #0 | Requirements: Find the regular expression that will match the above cases. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method |
| 2. Repetition Token #1 | Requirements: Find the regular expression that will match the above cases. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method |
| 3. Repetition Token #2 | Requirements: Find the regular expression that will match the above cases.Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method. |
| 4. Repetition Token #3 | Requirements: Find the regular expression that will match the above cases. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method |
| 5. Not quite HBTN yet | Requirements: The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method |
| 6. Call me maybe | Requirement: The regular expression must match a 10 digit phone number. |
| 7. OMG WHY ARE YOU SHOUTING?  | Requirement: The regular expression must be only matching: capital letters. |

`Advance:`

| Name | Description |
| ------ | ------ |
| 8. Textme | Requirements: Your script should output: [SENDER],[RECEIVER],[FLAGS].The sender phone number or name (including country code if present). The receiver phone number or name (including country code if present).The flags that were used |
| 9. Pass LinkedIn technical interview level0 | Requirements: Solve LinkedIn regex puzzle: https://engineering.linkedin.com/puzzle. Provide as an answer file a screenshot containing your contact information, including your Holberton email address. |