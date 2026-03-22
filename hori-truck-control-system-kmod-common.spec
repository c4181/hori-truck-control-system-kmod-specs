Name:           hori-truck-control-system-kmod-common
Version:        0.0.2
Release:        %autorelease
Summary:        Common files for the hori-truck-control-system kernel module
License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
BuildArch:      noarch

Source0:        https://github.com/LinuxGamesTV/hori_control_systems/archive/refs/tags/%{version}.tar.gz
Requires:       udev
Provides:       hori-truck-control-system-kmod-common = %{version}

%description
License, documentation, and udev rules for the hori-truck-control-system
kernel module.

%prep
%setup -q -n hori_control_systems-%{version}

%build
# nothing to build

%install
install -d %{buildroot}%{_defaultdocdir}/%{name}
install -m 644 README.md %{buildroot}%{_defaultdocdir}/%{name}/
install -d %{buildroot}%{_defaultlicensedir}/%{name}
install -m 644 LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/
install -d %{buildroot}%{_udevrulesdir}
install -m 644 udev/*.rules %{buildroot}%{_udevrulesdir}/

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/*.rules

%post
udevadm control --reload-rules
udevadm trigger

%postun
udevadm control --reload-rules

%changelog
