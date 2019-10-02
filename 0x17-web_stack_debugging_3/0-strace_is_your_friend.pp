# Replace a line inside a file

file { '/var/www/html/wp-settings.php':
  ensure => 'present',
}

-> exec { 'replace':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', 'usr/sbin', '/bin' ],
}
