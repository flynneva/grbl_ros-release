%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-grbl-ros
Version:        0.0.16
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS grbl_ros package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-grbl-msgs
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyserial
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-galactic-ament-copyright
BuildRequires:  ros-galactic-ament-flake8
BuildRequires:  ros-galactic-ament-pep257
BuildRequires:  ros-galactic-grbl-msgs
BuildRequires:  ros-galactic-rclpy
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS2 package to interface with a GRBL serial device

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Sat Nov 27 2021 Evan Flynn <evanflynn.msu@gmail.com> - 0.0.16-1
- Autogenerated by Bloom

* Tue Apr 20 2021 Evan Flynn <evanflynn.msu@gmail.com> - 0.0.15-2
- Autogenerated by Bloom

