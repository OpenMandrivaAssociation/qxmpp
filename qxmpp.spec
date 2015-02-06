%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	XMPP client library based on Qt
Name:		qxmpp
Version:	0.7.5
Release:	2
License:	LGPLv2.1+ and Creative Commons Attribution
Group:		System/Libraries
Url:		http://code.google.com/p/qxmpp/
Source0:	http://qxmpp.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		qxmpp-0.6.3.1-dynamiclib.patch
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
%{_libdir}/libqxmpp.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{devname}
Summary:	QXmpp development files
Group:		Development/C++
Requires:	qt4-devel
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < 0.7.5

%description -n %{devname}
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

This package contains files required for development.

%files -n %{devname}
%doc AUTHORS CHANGELOG LICENSE.LGPL README
%doc %{_docdir}/%{name}
%{_includedir}/qxmpp
%{_libdir}/libqxmpp.so
%{_libdir}/pkgconfig/qxmpp.pc

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	QMAKE_CXXFLAGS_RELEASE= 
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

