#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	JSON-GLib - a library providing serialization and deserialization support for the JSON format
Summary(pl.UTF-8):	JSON-GLib - biblioteka zapewniająca serializację i deserializację dla formatu JSON
Name:		json-glib
Version:	1.6.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/json-glib/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	8df85e21e6fde3dc6e2f5d5929f7df99
URL:		https://wiki.gnome.org/Projects/JsonGlib
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools >= 0.18
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.6}
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.55.3
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.54.0
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
Requires:	glib2-devel >= 1:2.54.0

%description devel
Header files for the json-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki json-glib.

%package static
Summary:	Static json-glib library
Summary(pl.UTF-8):	Statyczna biblioteka json-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static json-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka json-glib.

%package apidocs
Summary:	json-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API json-glib
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
json-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API json-glib.

%prep
%setup -q

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=enabled} \
	-Dintrospection=enabled \
	-Dman=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%{__rm} -r $RPM_BUILD_ROOT{%{_libexecdir},%{_datadir}}/installed-tests/json-glib-1.0

%find_lang %{name}-1.0

%if %{with apidocs}
# FIXME: where to package gi-docgen generated docs?
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/json-glib-1.0 $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc NEWS README.md
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libjson-glib-1.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/json-glib-1.0
%endif
