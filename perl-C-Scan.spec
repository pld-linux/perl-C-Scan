#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	C
%define		pnam	Scan
Summary:	C::Scan - scan C language files for easily recognized constructs
Summary(pl.UTF-8):	C::Scan - poszukiwanie łatwo rozpoznawalnych konstrukcji w plikach w języku C
Name:		perl-C-Scan
Version:	0.74
Release:	10
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a229ce3836ba72f9b4cc3d1fb6392edb
URL:		http://search.cpan.org/dist/C-Scan/
BuildRequires:	perl-Data-Flow
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C::Scan Perl module scans C language files for easily recognized
constructs.

%description -l pl.UTF-8
C::Scan jest modułem Perla poszukującym łatwo rozpoznawalnych
konstrukcji w plikach w języku C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/C
%{_mandir}/man3/*
