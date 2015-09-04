%define		kdeframever	5.13
%define		qtver		5.3.2
%define		kfname		kiconthemes

Summary:	Icon GUI utilities
Name:		kf5-%{kfname}
Version:	5.13.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	109d43b5e45fe5ec9c355a73b5bb87a3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This library contains classes to improve the handling of icons in
applications using the KDE Frameworks. Provided are:

- KIconDialog: Dialog class to let the user select an icon from the
  list of installed icons.
- KIconButton: Custom button class that displays an icon. When
  clicking it, the user can change it using the icon dialog.
- KIconEffect: Applies various colorization effects to icons, which
  can be used to create selected/disabled icon images.

Other classes in this repository are used internally by the icon theme
configuration dialogs, and should not be used by applications.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kiconfinder5
%attr(755,root,root) %ghost %{_libdir}/libKF5IconThemes.so.5
%attr(755,root,root) %{_libdir}/libKF5IconThemes.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIconThemes
%{_includedir}/KF5/kiconthemes_version.h
%{_libdir}/cmake/KF5IconThemes
%attr(755,root,root) %{_libdir}/libKF5IconThemes.so
%{qt5dir}/mkspecs/modules/qt_KIconThemes.pri
