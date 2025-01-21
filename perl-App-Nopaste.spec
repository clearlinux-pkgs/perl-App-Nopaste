#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-App-Nopaste
Version  : 1.013
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-1.013.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/App-Nopaste-1.013.tar.gz
Summary  : 'Easy access to any pastebin'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-App-Nopaste-bin = %{version}-%{release}
Requires: perl-App-Nopaste-license = %{version}-%{release}
Requires: perl-App-Nopaste-man = %{version}-%{release}
Requires: perl-App-Nopaste-perl = %{version}-%{release}
Requires: perl(Class::Load)
Requires: perl(Getopt::Long::Descriptive)
Requires: perl(JSON::MaybeXS)
Requires: perl(LWP::Protocol)
Requires: perl(LWP::UserAgent)
Requires: perl(Module::Pluggable)
Requires: perl(Module::Runtime)
Requires: perl(Path::Tiny)
Requires: perl(URI::Escape)
Requires: perl(WWW::Mechanize)
Requires: perl(namespace::clean)
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(Getopt::Long::Descriptive)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(JSON::MaybeXS)
BuildRequires : perl(LWP::Protocol)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Module::Pluggable)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Sub::Exporter::Util)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(URI::Escape)
BuildRequires : perl(WWW::Mechanize)
BuildRequires : perl(namespace::clean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution App-Nopaste,
version 1.013:
Easy access to any pastebin

%package bin
Summary: bin components for the perl-App-Nopaste package.
Group: Binaries
Requires: perl-App-Nopaste-license = %{version}-%{release}

%description bin
bin components for the perl-App-Nopaste package.


%package dev
Summary: dev components for the perl-App-Nopaste package.
Group: Development
Requires: perl-App-Nopaste-bin = %{version}-%{release}
Provides: perl-App-Nopaste-devel = %{version}-%{release}
Requires: perl-App-Nopaste = %{version}-%{release}

%description dev
dev components for the perl-App-Nopaste package.


%package license
Summary: license components for the perl-App-Nopaste package.
Group: Default

%description license
license components for the perl-App-Nopaste package.


%package man
Summary: man components for the perl-App-Nopaste package.
Group: Default

%description man
man components for the perl-App-Nopaste package.


%package perl
Summary: perl components for the perl-App-Nopaste package.
Group: Default
Requires: perl-App-Nopaste = %{version}-%{release}

%description perl
perl components for the perl-App-Nopaste package.


%prep
%setup -q -n App-Nopaste-1.013
cd %{_builddir}/App-Nopaste-1.013

%build
## build_prepend content
export PERL_MM_USE_DEFAULT=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-App-Nopaste
cp %{_builddir}/App-Nopaste-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-App-Nopaste/02baa9a7c1e8cd4e565c56a6af13a63d650805ef || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nopaste

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::Nopaste.3
/usr/share/man/man3/App::Nopaste::Command.3
/usr/share/man/man3/App::Nopaste::Service.3
/usr/share/man/man3/App::Nopaste::Service::Codepeek.3
/usr/share/man/man3/App::Nopaste::Service::Debian.3
/usr/share/man/man3/App::Nopaste::Service::Gist.3
/usr/share/man/man3/App::Nopaste::Service::GitLab.3
/usr/share/man/man3/App::Nopaste::Service::Mojopaste.3
/usr/share/man/man3/App::Nopaste::Service::PastebinCom.3
/usr/share/man/man3/App::Nopaste::Service::Pastie.3
/usr/share/man/man3/App::Nopaste::Service::Shadowcat.3
/usr/share/man/man3/App::Nopaste::Service::Snitch.3
/usr/share/man/man3/App::Nopaste::Service::Ubuntu.3
/usr/share/man/man3/App::Nopaste::Service::ssh.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-App-Nopaste/02baa9a7c1e8cd4e565c56a6af13a63d650805ef

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nopaste.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
