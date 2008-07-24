%define name ifled
%define version 0.6
%define release %mkrel 13

Summary:   Flash kbd LEDs to indicate network interface traffic
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:	   http://www.sudac.org/~napolium/linux/
Source0:   %{name}-%{version}.tar.bz2
Source1:   %{name}-%{version}-extra.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Group:     Monitoring
Conflicts: ifled-nl
Requires(pre):		rpm-helper

%description
InterfaceLED is a program that uses the keybord LEDs to indicated various
things about a specified interface. For example if a network card is sending
or receiveing data.

%prep
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}

%setup -T -b 0
%setup -T -D -a 1

%build
  make CFLAGS="${RPM_OPT_FLAGS}"

%install
  mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_initrddir}}
  mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
  install -s ifled $RPM_BUILD_ROOT%{_bindir}
  cp %{name}-%{version}-extra/ifled_init_script ${RPM_BUILD_ROOT}%{_initrddir}/ifled
  cp %{name}-%{version}-extra/ifled_sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/ifled

%clean
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}

%post
  %_post_service  %{name}

%preun
  %_preun_service  %{name}

%files
%defattr(-,root,root,755)
%doc ChangeLog README %{name}-%{version}-extra/README.init-script
%{_bindir}/ifled
%{_initrddir}/ifled
%config(noreplace) %{_sysconfdir}/sysconfig/ifled

