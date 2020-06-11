"""Role testing files using testinfra."""
def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
def test_redis_installed(host):
    redis_package_name = _get_redis_package_name(host.system_info.distribution)
    redis_package = host.package(redis_package_name)
    assert redis_package.is_installed
def test_redis_service_started_enabled(host):
    redis_service_name = _get_redis_package_name(host.system_info.distribution)
    redis_service = host.service(redis_service_name)
    assert redis_service.is_running
    assert redis_service.is_enabled
def _get_redis_package_name(host_distro):
    return {
        "ubuntu": "redis-server",
        "debian": "redis-server",
        "centos": "redis"
    }.get(host_distro, "redis")
