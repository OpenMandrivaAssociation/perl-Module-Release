
%define realname   Module-Release
%define version    1.20
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Automate software releases
Source:     http://www.cpan.org/modules/by-module/Module/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ConfigReader::Simple)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTTP::Message)
BuildRequires: perl(IO::Null)
BuildRequires: perl(Net::FTP)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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
%perl_vendorlib/*
/usr/bin/release
/usr/share/man/man1/release.1.lzma

