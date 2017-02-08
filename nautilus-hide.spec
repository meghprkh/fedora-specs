Name:           nautilus-hide
Version:        0.2.0
Release:        1%{?dist}
Summary:         Extension for Nautilus to hide files without renaming them

License:        GPLv3
URL:            https://github.com/brunonova/nautilus-hide
Source0:        https://github.com/brunonova/nautilus-hide/archive/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  xdotool
Requires:       gettext
Requires:       nautilus-python
Requires:       xdotool

%description
Nautilus Hide is a simple Python extension for the Nautilus file manager that
adds options to the right-click menu to hide or unhide files.

The extension
hides the files without renaming them (i.e. without prefixing a dot (.) or
suffixing a tilde (~)). It does that by adding their names to the folder's
".hidden" file, which Nautilus reads to hide the listed files the next time
you open or refresh the folder.

%global debug_package %{nil}

%prep
%autosetup


%build

%cmake .
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README.md 
%license LICENSE 

%{_datadir}/locale/pt/LC_MESSAGES/nautilus-hide.mo
%{_datadir}/locale/fr/LC_MESSAGES/nautilus-hide.mo
%{_datadir}/nautilus-python/extensions/nautilus-hide.*

%changelog
* Thu Feb 9 2017 Megh Parikh <meghprkh@gmail.com>
- Initial package
