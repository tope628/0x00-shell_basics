#create a file using puppet

file { '/tmp/holberton':
ensure  => file,
content => 'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data'
}
