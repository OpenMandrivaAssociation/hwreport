Summary:	Collect system informations for the hardware4linux.info site
Name:		hwreport
Version:	0.9.4
Release:	%mkrel 1
Source0:	http://hardware4linux.info/res/%{name}-%{version}.tar.bz2
License:	GPL
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
