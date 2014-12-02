#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Module
%define	pnam	Find
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Find - Find and use installed modules in a (sub)category
Summary(pl.UTF-8):	Module::Find - wyszukiwanie i używanie modułów w (pod)kategorii
Name:		perl-Module-Find
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/CRENZ/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abd614f3ebca68b4e7cc474400a8c0f2
URL:		http://search.cpan.org/dist/Module-Find/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.04
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Find lets you find and use modules in categories. This can be
very useful for auto-detecting driver or plugin modules. You can
differentiate between looking in the category itself or in all
subcategories.

%description -l pl.UTF-8
Module::Find pozwala odnaleźć i używać moduly w kategoriach. Może to
być bardzo przydatne do automatycznego wykrywania modułów sterowników
lub wtyczek. Można rozróżnić pomiędzy szukaniem w ramach samej
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
%{_mandir}/man3/Module::Find.3pm*
