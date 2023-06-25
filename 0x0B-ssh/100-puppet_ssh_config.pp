# set sh_config file.
file_line { 'Declare_identity_file':
  path  => '/home/user/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  owner => 'user',
  group => 'user',
  mode  => '0600',
}

file_line { 'Turn_off_passwd_auth':
  path  => '/home/user/.ssh/config',
  line  => 'PasswordAuthentication no',
  owner => 'user',
  group => 'user',
  mode  => '0600',
}
