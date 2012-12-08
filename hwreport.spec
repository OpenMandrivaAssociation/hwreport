Summary:	Collect system informations for the hardware4linux.info site
Name:		hwreport
Version:	0.10.0
Release:	%mkrel 9
Source0:	http://hardware4linux.info/res/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://hardware4linux.info/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	dmidecode pciutils
Provides: lsb-hardware4linux.info-collector

%description
Collect system informations for the hardware4linux.info site.

%prep
%setup -q

%build
gcc %{optflags} -o scan-printers scan-printers.c

%install
rm -rf %{buildroot}
install -m755 scan-printers -D %{buildroot}%{_bindir}/scan-printers
install -m755 hwreport -D %{buildroot}%{_sbindir}/hwreport
#install -m755 osinfo -D %{buildroot}%{_bindir}/osinfo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/scan-printers
%{_sbindir}/hwreport
#%{_bindir}/osinfo


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-7mdv2011.0
+ Revision: 665489
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-6mdv2011.0
+ Revision: 605888
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-5mdv2010.1
+ Revision: 522889
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10.0-4mdv2010.0
+ Revision: 425194
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.10.0-3mdv2009.1
+ Revision: 351240
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.10.0-2mdv2009.0
+ Revision: 264661
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.10.0-1mdv2009.0
+ Revision: 206549
- New version 0.10.0

* Tue Jan 08 2008 Thierry Vignaud <tv@mandriva.org> 0.9.4-2mdv2008.1
+ Revision: 146800
- require pciutils
- provides lsb-hardware4linux.info-collector
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 0.9.4-1mdv2008.0
+ Revision: 71839
- New version 0.9.4

* Fri Aug 10 2007 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 61426
- New version 0.9.3

* Mon Jul 23 2007 Funda Wang <fwang@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 54524
- New version

* Fri Jul 20 2007 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2008.0
+ Revision: 53844
- New version

* Mon Jul 02 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.8-1mdv2008.0
+ Revision: 47097
- Import hwreport

