%global octpkg pkg-octave-doc

Summary:	Octave Package Documentation
Name:		octave-pkg-octave-doc
Version:	0.5.3
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/pkg-octave-doc/
Url:		https://github.com/gnu-octave/pkg-octave-doc/
Source0:	https://github.com/gnu-octave/pkg-octave-doc/archive/refs/tags/release-%{version}/pkg-octave-doc-%{version}.tar.gz

BuildRequires:  octave-devel >= 7.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Octave Package Documentation

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-release-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

