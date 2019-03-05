import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vim_installed(host):
    distribution = host.system_info.distribution
    if distribution == 'centos':
        pkg = 'vim-enhanced'
    elif distribution == 'ubuntu':
        pkg = 'vim'

    assert host.package(pkg).is_installed


def test_config_file(host):
    distribution = host.system_info.distribution
    if distribution == 'centos':
        fname = '/etc/vimrc'
    elif distribution == 'ubuntu':
        fname = '/etc/vim/vimrc'

    f = host.file(fname)

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
