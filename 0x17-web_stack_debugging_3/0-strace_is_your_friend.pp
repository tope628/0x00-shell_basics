#fix apache 500 error

exec { 'apache':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin',
}
