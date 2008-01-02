%define module	Term-ProgressBar
%define version 2.09
%define release %mkrel 2

Summary:	Provides a progress meter on a standard terminal
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Class::MethodMaker)
BuildRequires:	perl(Term::ReadKey)

%description
Term::ProgressBar provides a simple progress bar on the terminal, to
let the user know that something is happening, roughly how much stuff
has been done, and maybe an estimate at how long remains.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc README Changes
%{perl_vendorlib}/Term/ProgressBar.pm
%{_mandir}/*/*


