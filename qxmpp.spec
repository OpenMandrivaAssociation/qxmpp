%define libname %mklibname qxmpp 1
%define devname %mklibname -d qxmpp

Name:		qxmpp
Version:	1.2.0
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
BuildRequires:	cmake(Qt5Xml)

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
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libqxmpp.so.*

%files -n %{devname}
%{_includedir}/qxmpp
%{_libdir}/cmake/qxmpp
%{_libdir}/pkgconfig/qxmpp.pc
%{_libdir}/*.so
