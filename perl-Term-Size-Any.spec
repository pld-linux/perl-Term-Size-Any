#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Term
%define	pnam	Size-Any
Summary:	Term::Size::Any - Retrieve terminal size
#Summary(pl.UTF-8):
Name:		perl-Term-Size-Any
Version:	0.001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	58722dad73c6965d5c4b975e3ae47116
URL:		http://search.cpan.org/dist/Term-Size-Any/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Devel::Hide)
BuildRequires:	perl(Term::Size::Perl)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a unified interface to retrieve terminal size. It loads one
module of a list of known alternatives, each implementing some way to
get the desired terminal information. This loaded module will actually
do the job on behalf of Term::Size::Any.

Thus, Term::Size::Any depends on the availability of one of these
modules:

Term::Size (soon to be supported) Term::Size::Perl Term::Size::ReadKey
(soon to be supported) Term::Size::Win32

This release fallbacks to Term::Size::Win32 if running in Windows 32
systems. For other platforms, it uses the first of Term::Size::Perl,
Term::Size or Term::Size::ReadKey which loads successfully. (To be
honest, I disabled the fallback to Term::Size and Term::Size::ReadKey
which are buggy by now.)

# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/Size/*.pm
%{_mandir}/man3/*
