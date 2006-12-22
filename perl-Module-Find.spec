#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Find
Summary:	Module::Find - Find and use installed modules in a (sub)category
Summary(pl):	Module::Find - wyszukiwanie i u¿ywanie modu³ów w (pod)kategorii
Name:		perl-Module-Find
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1b756c84e476fc8179fcf2699a4d1a86
URL:		http://search.cpan.org/dist/Module-Find/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Find lets you find and use modules in categories. This can be
very useful for auto-detecting driver or plugin modules. You can
differentiate between looking in the category itself or in all
subcategories.

%description -l pl
Module::Find pozwala odnale¼æ i u¿ywaæ moduly w kategoriach. Mo¿e to
byæ bardzo przydatne do automatycznego wykrywania modu³ów sterowników
lub wtyczek. Mo¿na rozró¿niæ pomiêdzy szukaniem w ramach samej
kategorii lub we wszystkich podkategoriach.

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
%doc Changes README
%{perl_vendorlib}/Module/Find.pm
%{_mandir}/man3/*
