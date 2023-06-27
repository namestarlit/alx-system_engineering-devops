# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 'https://www.youtube.com/watch?v=QH2-TGUlwu4';
      }
    }
  ",
  notify  => Service['nginx'],
}

# Enable and start Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
