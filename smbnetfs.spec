Summary:	SMBNetFS
Summary(pl.UTF-8):	SMBNetFS
Name:		smbnetfs
Version:	0.3.10
Release:	0.3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/smbnetfs/%{name}-%{version}.tar.bz2
# Source0-md5:	90835704e814e73e451c51a387e9d3b7
URL:		http://sourceforge.net/projects/smbnetfs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsmbclient-devel >= 3.0.21
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMBNetFS is a Linux/FreeBSD filesystem that allow you to use
samba/microsoft network in the same manner as the network neighborhood
in Microsoft Windows.

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
%doc AUTHORS ChangeLog README TODO doc/INSTALL doc/RUSSIAN.FAQ doc/smbnetfs.conf
%attr(755,root,root) %{_bindir}/*
