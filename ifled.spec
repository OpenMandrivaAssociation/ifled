%define name ifled
%define version 0.6
%define release 13

Summary:   Flash kbd LEDs to indicate network interface traffic
Name:      %{name}
Version:   %{version}
Release:   %{release}
URL:	   http://www.sudac.org/~napolium/linux/
Source0:   %{name}-%{version}.tar.bz2
Source1:   %{name}-%{version}-extra.tar.bz2
patch0:    ifled-0.6.printf.patch
License: GPLv2+
Group:     Monitoring
Conflicts: ifled-nl
Requires(pre):		rpm-helper

%description
InterfaceLED is a program that uses the keybord LEDs to indicated various
things about a specified interface. For example if a network card is sending
or receiveing data.

%prep
%setup -T -b 0
%setup -T -D -a 1
%patch0 -p1 -b .printf

%build
  make CFLAGS="${RPM_OPT_FLAGS}"

%install
  mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_initrddir}}
  mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
  install ifled $RPM_BUILD_ROOT%{_bindir}
  cp %{name}-%{version}-extra/ifled_init_script ${RPM_BUILD_ROOT}%{_initrddir}/ifled
  cp %{name}-%{version}-extra/ifled_sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/ifled

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



%changelog
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6-13mdv2009.0
+ Revision: 247208
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6-11mdv2008.1
+ Revision: 126995
- kill re-definition of %%buildroot on Pixel's request
- import ifled


* Thu Feb 02 2005 Lenny Cartier <lenny@mandriva.com> 0.6-11mdk
- rebuild

* Fri Dec 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-10mdk
- new initscript by Bruno Teixeira Santos

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-9mdk
- rebuild

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6-8mdk
- rebuild

* Thu Oct 10 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.6-7mdk
- rebuild

* Tue Sep 11 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.6-6mdk
- fixes from Maxim Heijndijk <cchq@wanadoo.nl> :
	- Added init script.
	- Added /etc/sysconfig/ifled configfile.

* Wed Aug 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.6-5mdk
- rebuild

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.6-4mdk
- rebuild

* Thu Sep 07 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.6-3mdk
- remove packager tag

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-2mdk
- BM

* Thu Jun 22 2000 Max Heijndijk <cchq@wanadoo.nl> 0.6-1mdk
- Made package relocatable
- Added "make ${RPM_OPT_FLAGS}"
- bzipped source

* Sat Dec 11 1999 <bet@mordor.net>
- Initial Wrap
