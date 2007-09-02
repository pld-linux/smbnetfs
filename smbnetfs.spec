Summary:	SMBNetFS - using Samba/Microsoft Network as a regular filesystem
Summary(pl.UTF-8):	SMBNetFS - używanie Samby/Microsoft Network jako zwykłego systemu plików
Name:		smbnetfs
Version:	0.3.10
Release:	0.3
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smbnetfs/%{name}-%{version}.tar.bz2
# Source0-md5:	90835704e814e73e451c51a387e9d3b7
URL:		http://sourceforge.net/projects/smbnetfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 2.5
BuildRequires:	libsmbclient-devel >= 3.0.21
BuildRequires:	pkgconfig
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMBNetFS is a Linux/FreeBSD filesystem that allow you to use
Samba/Microsoft Network in the same manner as the Network Neighborhood
in Microsoft Windows.

%description -l pl.UTF-8
SMBNetFS to system plików dla Linuksa/FreeBSD pozwalający używać Samby
lub sieci Microsoft Network w ten sam sposób, co Otoczenia sieciowego
w systemie Microsoft Windows.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/INSTALL doc/smbnetfs.conf
%lang(ru) %doc doc/RUSSIAN.FAQ
%attr(755,root,root) %{_bindir}/*
