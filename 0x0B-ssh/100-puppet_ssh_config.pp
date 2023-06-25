# ssh_config file
file {'/home/ubuntu/.ssh/config':
  ensure    => present,
  mode      => '0600',
  owner     => 'ubuntu',
  group     => 'ubuntu',
  content   => "
  Host 52.87.155.27
	  IdentityFile ~/.ssh/school
	  PasswordAuthentication no
  ",
  show_diff => true,
}
