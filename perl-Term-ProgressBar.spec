%define upstream_name	 Term-ProgressBar
%define upstream_version 2.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Provides a progress meter on a standard terminal
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Term/Term-ProgressBar-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::MethodMaker)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Capture::Tiny)
BuildArch:	noarch

%description
Term::ProgressBar provides a simple progress bar on the terminal, to
let the user know that something is happening, roughly how much stuff
has been done, and maybe an estimate at how long remains.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Term/ProgressBar.pm
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.0
+ Revision: 401605
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-5mdv2009.0
+ Revision: 258506
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.09-4mdv2009.0
+ Revision: 246518
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.09-2mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.09-2mdv2007.0
+ Revision: 100116
- Import perl-Term-ProgressBar

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.09-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
	- URL

* Sun Jul 17 2005 Stefan van der Eijk <stefan@eijk.nu> 2.09-1mdk
- 2.09
- mkrel

* Mon Jan 17 2005 Stefan van der Eijk <stefan@mandrakesoft.com> 2.06-0.r1.1mdk
- New release 2.06-r1


