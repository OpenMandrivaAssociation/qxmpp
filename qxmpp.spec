%define oldlibname %mklibname qxmpp 1
%define libname %mklibname qxmpp
%define devname %mklibname -d qxmpp

Name:		qxmpp
Version:	1.13.0
Release:	1
Summary:	Library for using the XMPP messenging protocol with Qt
Url:		https://invent.kde.org/libraries/qxmpp
Source0:	https://invent.kde.org/libraries/qxmpp/-/archive/v%{version}/qxmpp-v%{version}.tar.bz2
License:	LGPLv2.1
Group:		Applications/Productivity
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
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
# 2026-01-05, after 6.0
%rename %{oldlibname}

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
%{_libdir}/libQXmppQt6.so.7
%{_libdir}/libQXmppOmemoQt6.so.%{version}
%{_libdir}/libQXmppOmemoQt6.so.7

%files -n %{devname}
%{_includedir}/QXmppQt6/
%{_libdir}/cmake/QXmppQt6/
%{_libdir}/cmake/QXmppOmemoQt6/
%{_libdir}/pkgconfig/QXmppQt6.pc
%{_libdir}/*.so
