%include	/usr/lib/rpm/macros.perl
%define		pdir	C
%define		pnam	Scan
Summary:	C::Scan Perl module
Summary(cs):	Modul C::Scan pro Perl
Summary(da):	Perlmodul C::Scan
Summary(de):	C::Scan Perl Modul
Summary(es):	Módulo de Perl C::Scan
Summary(fr):	Module Perl C::Scan
Summary(it):	Modulo di Perl C::Scan
Summary(ja):	C::Scan Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	C::Scan ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul C::Scan
Summary(pl):	Modu³ Perla C::Scan
Summary(pt):	Módulo de Perl C::Scan
Summary(pt_BR):	Módulo Perl C::Scan
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl C::Scan
Summary(sv):	C::Scan Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl C::Scan
Summary(zh_CN):	C::Scan Perl Ä£¿é
Name:		perl-C-Scan
Version:	0.74
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a229ce3836ba72f9b4cc3d1fb6392edb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Data-Flow
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C::Scan - scan C language files for easily recognized constructs.

%description -l cs
Modul C::Scan pro Perl.

%description -l da
Perlmodul C::Scan.

%description -l de
C::Scan Perl Modul.

%description -l es
Módulo de Perl C::Scan.

%description -l fr
Module Perl C::Scan.

%description -l it
Modulo di Perl C::Scan.

%description -l ja
C::Scan Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
C::Scan ÆÞ ¸ðÁÙ.

%description -l nb
Perlmodul C::Scan.

%description -l pl
C::Scan - modu³ poszukuj±cy ³atwo rozpoznawalnych konstrukcji w
plikach w jêzyku C.

%description -l pt
Módulo de Perl C::Scan.

%description -l pt_BR
Módulo Perl C::Scan.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl C::Scan.

%description -l sv
C::Scan Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl C::Scan.

%description -l zh_CN
C::Scan Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/C
%{_mandir}/man3/*
