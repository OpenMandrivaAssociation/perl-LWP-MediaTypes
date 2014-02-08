%define upstream_name    LWP-MediaTypes
%define upstream_version 6.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:    Media types and mailcap processing
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: noarch


%description
This module provides functions for handling media (also known as MIME)
types and encodings. The mapping from file extensions to media types is
defined by the _media.types_ file. If the _~/.media.types_ file exists it
is used instead. For backwards compatibility we will also look for
_~/.mime.types_.

The following functions are exported by default:

* guess_media_type( $filename )

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-4mdv2012.0
+ Revision: 765394
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-3
+ Revision: 763910
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-2
+ Revision: 763087
- rebuild

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.10.0-1
+ Revision: 664978
- import perl-LWP-MediaTypes

