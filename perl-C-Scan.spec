%include	/usr/lib/rpm/macros.perl
Summary:	C-Scan perl module
Summary(pl):	Modu³ perla C-Scan
Name:		perl-C-Scan
Version:	0.74
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/C/C-Scan-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Data-Flow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C-Scan - scan C language files for easily recognized constructs.

%description -l pl
Modu³ perla C-Scan.

%prep
%setup -q -n C-Scan-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/C/Scan.pm
%{_mandir}/man3/*
