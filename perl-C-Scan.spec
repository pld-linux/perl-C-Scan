%include	/usr/lib/rpm/macros.perl
Summary:	C-Scan perl module
Summary(pl):	Modu³ perla C-Scan
Name:		perl-C-Scan
Version:	0.51
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/C/C-Scan-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-12
BuildRequires:	perl-Data-Flow
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
C-Scan - scan C language files for easily recognized constructs.

%description -l pl
Modu³ perla C-Scan.

%prep
%setup -q -n C-Scan-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/C/Scan
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.gz

%{perl_sitelib}/C/Scan.pm
%{perl_sitearch}/auto/C/Scan

%{_mandir}/man3/*
