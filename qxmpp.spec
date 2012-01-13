%define name	qxmpp
%define major	1
%define libname	%mklibname %{name} %{major}

Name:		%{name}
Summary:	XMPP client library based on Qt
Version:	0.3.91
Release:	1
License:	LGPLv2.1+ and Creative Commons Attribution
Group:		System/Libraries
Source0:	http://qxmpp.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		qxmpp-0.3.91-mdv-dynamiclib.patch
BuildRequires:	qt4-devel

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is
the only third party library it is dependent on. Users need to a have working
knowledge of C++ and Qt basics (Signals and Slots and Qt data types).
The underlying TCP socket and the XMPP RFCs (RFC3920 and RFC3921) have been
encapsulated into classes and functions. Therefore the user would not be
bothered with these details. But it is always recommended to the advanced users
to read and enjoy the low level details.

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	XMPP client library based on Qt
Group:		System/Libraries

%description -n %{libname}
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is
the only third party library it is dependent on. Users need to a have working
knowledge of C++ and Qt basics (Signals and Slots and Qt data types).
The underlying TCP socket and the XMPP RFCs (RFC3920 and RFC3921) have been
encapsulated into classes and functions. Therefore the user would not be
bothered with these details. But it is always recommended to the advanced users
to read and enjoy the low level details.

%files -n %{libname}
%_qt_libdir/libqxmpp.so.%{major}*

#------------------------------------------------------------------------------

%package devel
Summary:	QXmpp development files
Group:		Development/C++

%description devel
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

This package contains files required for development.

%files devel
%{_qt_includedir}/qxmpp
%{_libdir}/libqxmpp.so
%{_libdir}/pkgconfig/qxmpp.pc
%{_qt_docdir}/%{name}
%doc AUTHORS CHANGELOG LICENSE.LGPL README

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%{qmake_qt4}
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
install -d %{buildroot}%{_qt_docdir}
mv %{buildroot}/usr/lib/qt4/share/doc/qxmpp %{buildroot}%{_qt_docdir}/%{name}
rm -rf %{buildroot}/usr/lib/qt4/share
%ifarch x86_64
mv %{buildroot}/usr/lib/pkgconfig %{buildroot}%{_libdir}
%endif
