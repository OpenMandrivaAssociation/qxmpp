%define libname %mklibname qxmpp 1
%define devname %mklibname -d qxmpp

Name:		qxmpp
Version:	1.8.1
Release:	1
Summary:	Library for using the XMPP messenging protocol with Qt
Url:		https://github.com/qxmpp-project/qxmpp
Source0:	https://github.com/qxmpp-project/qxmpp/archive/v%{version}/%{name}-%{version}.tar.gz
License:	LGPLv2.1
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qca-qt5)

BuildRequires:          pkgconfig(libprotobuf-c)
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

%prep
%autosetup -p1
%cmake_kde5 \
            -DBUILD_OMEMO=ON \
            -DWITH_GSTREAMER=ON \
            -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
#{_libdir}/libqxmpp.so.*
%{_libdir}/libQXmppQt5.so.%{version}
%{_libdir}/libQXmppQt5.so.5
%{_libdir}/libQXmppOmemoQt5.so.%{version}
%{_libdir}/libQXmppOmemoQt5.so.5

%files -n %{devname}
%{_includedir}/QXmppQt5/
%{_libdir}/cmake/QXmpp/
%{_libdir}/cmake/QXmppQt5/
%{_libdir}/cmake/QXmppOmemoQt5/
%{_libdir}/pkgconfig/qxmpp.pc
%{_libdir}/pkgconfig/QXmppQt5.pc
%{_libdir}/*.so
