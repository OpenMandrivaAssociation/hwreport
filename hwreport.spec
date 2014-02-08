Summary:	Collect system informations for the hardware4linux.info site
Name:		hwreport
Version:	0.11.0
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://hardware4linux.info/
Source0:	http://hardware4linux.info/res/%{name}-%{version}.tar.bz2
Requires:	dmidecode
Requires:	pciutils
Provides:	lsb-hardware4linux.info-collector

%description
Collect system informations for the hardware4linux.info site.

%prep
%setup -q

%build
gcc %{optflags} -o scan-printers scan-printers.c

%install
install -m755 scan-printers -D %{buildroot}%{_bindir}/scan-printers
install -m755 hwreport -D %{buildroot}%{_sbindir}/hwreport
#install -m755 osinfo -D %{buildroot}%{_bindir}/osinfo

%files
%{_bindir}/scan-printers
%{_sbindir}/hwreport
#%{_bindir}/osinfo

