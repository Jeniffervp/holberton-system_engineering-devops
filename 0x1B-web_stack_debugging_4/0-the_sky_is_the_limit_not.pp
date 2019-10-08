file { '/etc/default/nginx':
  ensure => 'present',
}

-> exec { 'replace':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => ['/usr/bin', 'usr/sbin', '/bin' ],
}

-> exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin','/usr/sbin'],
}