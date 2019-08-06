# Execute a command using exec

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
