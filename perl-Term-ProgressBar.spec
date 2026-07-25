%define upstream_name	 Term-ProgressBar
%define upstream_version 2.23

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Provides a progress meter on a standard terminal

License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://github.com/manwar/Term-ProgressBar
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Term-ProgressBar-%{upstream_version}.tar.gz

BuildRequires:	make
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
%{perl_vendorlib}/Term/ProgressBar/IO.pm


