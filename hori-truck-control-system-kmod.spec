%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

Name: hori-truck-control-system-kmod

Version:        0.0.2
Release:        %autorelease
Summary:        Driver for the Hori Truck Control System

Group:          System Environment/Kernel

License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
Source0:        https://github.com/LinuxGamesTV/hori_control_systems/archive/refs/tags/%{version}.tar.gz

BuildRequires:  kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
Kernel module for the HORI Control Systems HID driver (hid-hori). Supports
HORI steering wheels including all three pedals (gas, brake, clutch), the
shifter, hat switch, and analog stick mouse emulation.

Requires kernel 6.12 or higher. This driver is early alpha — use at your
own risk.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    cp -a hori_control_systems-%{version} _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
    install -d %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -m 755 _kmod_build_${kernel_version%%___*}/hid-hori-wheels.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -m 755 _kmod_build_${kernel_version%%___*}/hid-hori-multisticks.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%clean
rm -rf $RPM_BUILD_ROOT
