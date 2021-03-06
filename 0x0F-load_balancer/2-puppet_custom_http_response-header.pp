# create a file to automate the custom HTTP header
exec {'update_server':
command => '/usr/bin/apt-get update',
}
-> package {'nginx':
ensure => 'present',
}
-> file {'/etc/nginx/sites-available/default':
ensure => 'present',
}
-> file_line { 'check a line':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
line   => "   location / {
             add_header X-Served-By ${hostname};",
match  => '^\tlocation / {',
}
-> exec { 'start/restart server':
command => '/usr/sbin/service nginx restart',
}
