%define upstream_name	 Term-ProgressBar
%define upstream_version 2.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Provides a progress meter on a standard terminal
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Class::MethodMaker)
BuildRequires:	perl(Term::ReadKey)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
Term::ProgressBar provides a simple progress bar on the terminal, to
let the user know that something is happening, roughly how much stuff
has been done, and maybe an estimate at how long remains.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

