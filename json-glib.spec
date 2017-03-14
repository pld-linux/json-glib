Summary:	JSON-GLib - a library providing serialization and deserialization support for the JSON format
Summary(pl.UTF-8):	JSON-GLib - biblioteka zapewniająca serializację i deserializację dla formatu JSON
Name:		json-glib
Version:	1.2.6
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/json-glib/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	e4f21b2c56e7cce5362e36ab7bf0cef6
URL:		http://live.gnome.org/JsonGlib
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.37.6
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.37.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON-GLib is a library providing serialization and deserialization
support for the JavaScript Object Notation (JSON) format described by
RFC 4627.

%description -l pl.UTF-8
JSON-GLib to biblioteka zapewniająca obsługę serializacji i
deserializacji dla formatu JSON (JavaScript Object Notation) opisanego
w RFC 4627.

%package devel
Summary:	Header files for the json-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki json-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.37.6

%description devel
Header files for the json-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki json-glib.

%package apidocs
Summary:	json-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API json-glib
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
json-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API json-glib.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libjson-glib-1.0.la

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS
%attr(755,root,root) %{_bindir}/json-glib-format
%attr(755,root,root) %{_bindir}/json-glib-validate
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjson-glib-1.0.so.0
%{_libdir}/girepository-1.0/Json-1.0.typelib
%{_mandir}/man1/json-glib-format.1*
%{_mandir}/man1/json-glib-validate.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjson-glib-1.0.so
%{_datadir}/gir-1.0/Json-1.0.gir
%{_includedir}/json-glib-1.0
%{_pkgconfigdir}/json-glib-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/json-glib
