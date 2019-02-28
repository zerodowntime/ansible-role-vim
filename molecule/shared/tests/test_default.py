import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vim_installed(host):
    assert host.package("vim-minimal").is_installed


def test_config_file(host):
    f = host.file('/etc/vimrc')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    assert f.contains('set number')
    assert f.contains('set nospell')
    assert f.contains('set showbreak=+++')


def test_environment_file(host):
    f = host.file('/etc/environment')

    assert f.exists
    assert f.contains('EDITOR=vim')
