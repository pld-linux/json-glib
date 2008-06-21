Summary:	JSON-GLib - a library providing serialization and deserialization support for the JSON format
Name:		json-glib
Version:	0.6.2
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://folks.o-hand.com/~ebassi/sources/%{name}-%{version}.tar.gz
# Source0-md5:	d98f5580035ad0b37fa11896053a57af
URL:		http://live.gnome.org/JsonGlib
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON-GLib is a library providing serialization and deserialization
support for the JavaScript Object Notation (JSON) format described by
RFC 4627.

%package devel
Summary:	Header files for the json-glib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the json-glib library.

%package apidocs
Summary:	json-glib API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
json-glib API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_gtkdocdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{_datadir}/gtk-doc/html/%{name},%{_gtkdocdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjson-glib-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so
%{_libdir}/libjson-glib-1.0.la
%{_includedir}/json-glib-1.0
%{_pkgconfigdir}/json-glib-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/json-glib
