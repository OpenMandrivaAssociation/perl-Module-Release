%define upstream_name    Module-Release
%define upstream_version 2.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Automate software releases
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI)
BuildRequires:	perl(ConfigReader::Simple)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(HTTP::Message)
BuildRequires:	perl(IO::Null)
BuildRequires:	perl(Net::FTP)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Test::Without::Module)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README README
%{perl_vendorlib}/Module
%{_bindir}/release
%{_mandir}/man3/*
%{_mandir}/man1/release.1*

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-2mdv2011.0
+ Revision: 552000
- rebuild

* Thu Jun 18 2009 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.0
+ Revision: 386974
- update to 2.05
- using %%perl_convert_version
- fix license tag

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.04-1mdv2010.0
+ Revision: 369727
- adding missing prereq
- update to new version 2.04

* Sun Feb 08 2009 Jérôme Quelin <jquelin@mandriva.org> 2.02-1mdv2009.1
+ Revision: 338447
- update to new version 2.02

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2009.1
+ Revision: 307087
- update to new version 2.01

* Sat Sep 06 2008 Jérôme Quelin <jquelin@mandriva.org> 1.20-2mdv2009.0
+ Revision: 281841
- fix missing prereq not detected
- import perl-Module-Release


* Sat Sep 06 2008 cpan2dist 1.20-1mdv
- initial mdv release, generated with cpan2dist

