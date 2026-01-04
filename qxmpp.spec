%define libname %mklibname qxmpp 1
%define devname %mklibname -d qxmpp

Name:		qxmpp
Version:	1.10.2
Release:	1
Summary:	Library for using the XMPP messenging protocol with Qt
Url:		https://github.com/qxmpp-project/qxmpp
Source0:	https://github.com/qxmpp-project/qxmpp/archive/v%{version}/%{name}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qca-qt6)
BuildSystem:	cmake
BuildOption:	-DQT_VERSION_MAJOR=6
BuildOption:	-DBUILD_OMEMO=ON
BuildOption:	-DWITH_GSTREAMER=ON

BuildRequires:	pkgconfig(libprotobuf-c)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(libomemo-c)

%description
Library for using the XMPP messenging protocol with Qt

%package -n %{libname}
Summary:	Library for using the XMPP messenging protocol with Qt
Group:		System/Libraries

%description -n %{libname}
Library for using the XMPP messenging protocol with Qt

%package -n %{devname}
Summary:	Development files for QXmpp
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for QXmpp, a library for using the XMPP messenging
protocol with Qt

%files -n %{libname}
#{_libdir}/libqxmpp.so.*
%{_libdir}/libQXmppQt6.so.%{version}
%{_libdir}/libQXmppQt6.so.5
%{_libdir}/libQXmppOmemoQt6.so.%{version}
%{_libdir}/libQXmppOmemoQt6.so.5

%files -n %{devname}
%{_includedir}/QXmppQt6/
%{_libdir}/cmake/QXmppQt6/
%{_libdir}/cmake/QXmppOmemoQt6/
%{_libdir}/pkgconfig/QXmppQt6.pc
%{_libdir}/*.so
