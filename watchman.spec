Name:           watchman
Version:        4.7.0
Release:        1%{?dist}
Summary:        A file watching service

License:        Apache
URL:            https://facebook.github.io/watchman/
Source0:        https://github.com/facebook/watchman/archive/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python2-setuptools
BuildRequires:  python-devel

%description


%prep
%autosetup


%build
./autogen.sh

%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README.markdown 
%license LICENSE 
%{_bindir}/*
%{_libdir}/*
%{_defaultdocdir}/%{name}-%{version}/
/usr/var/run/%{name}/

%changelog
* Mon Sep 12 2016 Megh Parikh <meghprkh@gmail.com>
- Initial package
