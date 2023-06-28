# manifest to install and configure nginx server
# Usage: sudo puppet apply path/to/nginx.pp

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @(EOF)
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html;

      location / {
        try_files $uri $uri/ =404;
      }

      location /redirect_me {
        return 301 'https://www.youtube.com/watch?v=axlUv9evU2k';
      }

      # Redirect error page
      error_page 404 /404.html;
      location = /404.html {
        internal;
        default_type text/html;
        return 404 "Ceci n\'est pas une page\n";
      }
    }
  EOF
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

