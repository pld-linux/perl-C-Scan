#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	C
%define		pnam	Scan
Summary:	C::Scan - scan C language files for easily recognized constructs
Summary(pl):	C::Scan - poszukiwanie ³atwo rozpoznawalnych konstrukcji w plikach w jêzyku C
Name:		perl-C-Scan
Version:	0.74
Release:	8
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a229ce3836ba72f9b4cc3d1fb6392edb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Data-Flow
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C::Scan Perl module scans C language files for easily recognized
constructs.

%description -l pl
C::Scan jest modu³em Perla poszukuj±cym ³atwo rozpoznawalnych
konstrukcji w plikach w jêzyku C.

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
