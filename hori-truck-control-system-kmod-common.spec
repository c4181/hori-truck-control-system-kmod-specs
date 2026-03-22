Name:           hori-truck-control-system-kmod-common
Version:        0.0.2
Release:        1%{?dist}
Summary:        Common files for the hori-truck-control-system kernel module
License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
BuildArch:      noarch

Source0:        https://github.com/LinuxGamesTV/hori_control_systems/archive/refs/tags/%{version}.tar.gz

Provides:       hori-truck-control-system-kmod-common = %{version}

%description
License and documentation files for the hori-truck-control-system kernel module.

%prep
%setup -q -n hori_control_systems-%{version}

%build
# nothing to build

%install
install -d %{buildroot}%{_defaultdocdir}/%{name}
install -m 644 README.md %{buildroot}%{_defaultdocdir}/%{name}/
install -d %{buildroot}%{_defaultlicensedir}/%{name}
install -m 644 LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/

%files
%license LICENSE
%doc README.md

%changelog
