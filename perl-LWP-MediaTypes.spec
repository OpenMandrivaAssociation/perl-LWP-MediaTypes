%define modname	LWP-MediaTypes
%define modver 6.02

Summary:	Media types and mailcap processing
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/LWP/LWP-MediaTypes-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module provides functions for handling media (also known as MIME)
types and encodings. The mapping from file extensions to media types is
defined by the _media.types_ file. If the _~/.media.types_ file exists it
is used instead. For backwards compatibility we will also look for
_~/.mime.types_.

The following functions are exported by default:

* guess_media_type( $filename )

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*


