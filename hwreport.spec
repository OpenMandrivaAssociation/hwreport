Summary:	Collect system informations for the hardware4linux.info site
Name:		hwreport
Version:	0.8
Release:	%mkrel 1
Source0:	hwreport-%{version}.tar.bz2
License:	GPL
Group:		System/Kernel and hardware
Url:		http://hardware4linux.info/
Requires:	dmidecode

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
install -m755 osinfo -D %{buildroot}%{_bindir}/osinfo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/scan-printers
%{_sbindir}/hwreport
%{_bindir}/osinfo
