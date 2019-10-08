# Replace the number of hard no-file and soft no-file

file { '/etc/security/limits.conf':
  ensure => 'present',
}

-> exec { 'replace hard':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4096/g' /etc/security/limits.conf",
  path    => ['/usr/bin', 'usr/sbin', '/bin' ],
}

-> exec { 'replace soft':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/g' /etc/security/limits.conf",
  path    => ['/usr/bin', 'usr/sbin', '/bin' ],
}

-> exec { 'restart':
  command => 'sudo sysctl -p',
  path    => ['/usr/bin'],
}