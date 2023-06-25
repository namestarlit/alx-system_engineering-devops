# set sh_config file.
file_line { 'Declare_identity_file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  owner => 'user',
  group => 'user',
  mode  => '0600',
}

file_line { 'Turn_off_passwd_auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  owner => 'user',
  group => 'user',
  mode  => '0600',
}
