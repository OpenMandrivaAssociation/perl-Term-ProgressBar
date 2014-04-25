%define upstream_name	 Term-ProgressBar
%define upstream_version 2.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Provides a progress meter on a standard terminal

License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

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
%{perl_vendorlib}Term/ProgressBar/IO.pm


