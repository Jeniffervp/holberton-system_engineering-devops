# Create a file in tmp with permission, owner, grupo, and contains.

file { '/tmp/holberton':
  mode => 0744,
  group => www-data,
  owner => www-data,
  content => "I love Puppet",
}
