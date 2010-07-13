%define upstream_name    Module-Release
%define upstream_version 2.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Automate software releases
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI)
BuildRequires: perl(ConfigReader::Simple)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTTP::Message)
BuildRequires: perl(IO::Null)
BuildRequires: perl(Net::FTP)
BuildRequires: perl(Test::Output)
BuildRequires: perl(Test::Without::Module)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'Module::Release' automates your software release process. It started as a
script that automated my release process, so it has bits to talk to PAUSE
(CPAN) and SourceForge, and to use 'Makefile.PL' and 'CVS'. Other people
have extended this in other modules under the same namespace so you can use
'Module::Build', 'svn', and many other things.

The methods represent a step in the release process. Some of them check a
condition (e.g. all tests pass) and die if that doesn't work.
'Module::Release' doesn't let you continue if something is wrong. Once you
have checked everything, use the upload features to send your files to the
right places.

The included 'release' script is a good starting place. Don't be afraid to
edit it for your own purposes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README README
%{_mandir}/man3/*
%perl_vendorlib/Module
%_bindir/release
%_mandir/man1/release.1*

