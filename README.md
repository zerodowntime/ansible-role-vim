# environment

Ansible role to install vim editor

## Installation

```yaml
   ansible-galaxy install zerodowntime.environment
   ansible-galaxy install zerodowntime.vim
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
```

## Default role variables

| Variable name      | Required? |  Type  | Description             |
|:------------------ |:---------:|:------:|:----------------------- |
| vim__package_state |    yes    | string | package name to install |
| vim__package_name  |    yes    | string | installed package state |
| vim__rc            |    no     | string | vimrc plain text config |
| vim__env_editor    |    yes    |  bool  | can set env EDITOR=vim  |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

| Variable name         |  Type  | Description                     |
|:--------------------- |:------:|:------------------------------- |
| vim__vimrc_config     | string | vimrc config file               |
| vim__def_package_name | string | default package name to install |

**All static variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:

  - role: zerodowntime.vim
    vim__rc: |
      set number
      set showbreak=+++
      set nospell
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
