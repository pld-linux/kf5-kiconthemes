#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.104
%define		qtver		5.15.2
%define		kfname		kiconthemes

Summary:	Icon GUI utilities
Name:		kf5-%{kfname}
Version:	5.104.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	03ec7633a6f4e7c31fd2d212a83614aa
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Svg >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-karchive >= %{version}
Requires:	kf5-kconfigwidgets >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
Requires:	kf5-kitemviews >= %{version}
Requires:	kf5-kwidgetsaddons >= %{version}
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
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	cmake >= 3.16

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/kiconthemes.categories
%attr(755,root,root) %{_bindir}/kiconfinder5
%ghost %{_libdir}/libKF5IconThemes.so.5
%attr(755,root,root) %{_libdir}/libKF5IconThemes.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/iconengines/KIconEnginePlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kiconthemes5widgets.so
%{_datadir}/qlogging-categories5/kiconthemes.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIconThemes
%{_libdir}/cmake/KF5IconThemes
%{_libdir}/libKF5IconThemes.so
%{qt5dir}/mkspecs/modules/qt_KIconThemes.pri
