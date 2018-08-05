Name:           svkbd
Version:        0.1
Release:        0%{?dist}
Summary:        A simple virtual keyboard, intended to be used in environments, where no keyboard is available, or low memory requirements.
License:        MIT/X
URL:            https://github.com/taichifan/svkbd
Source0:        https://github.com/taichifan/svkbd/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.1-build.patch
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11
BuildRequires:  libX11-devel
BuildRequires:  libXtst
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  sed

%description

A simple virtual keyboard, intended to be used in environments, where no keyboard is available, or low memory requirements.

%prep
%setup -q
%patch0 -p1 -b .build

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%lang(en) %{_bindir}/%{name}-en

%changelog
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
Author: Marcel Schneider <marcel.schneider@studi.informatik.uni-stuttgart.de>
Date:   Sat Mar 1 14:14:07 2014 +0100

