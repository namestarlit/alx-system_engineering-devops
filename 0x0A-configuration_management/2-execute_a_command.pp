# Execute a command to kill process
exec {'pkill':
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  command => 'pkill -f ./killmenow',
}
