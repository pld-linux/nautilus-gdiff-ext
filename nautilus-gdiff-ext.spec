%define     realname    gdiff-ext
Summary:	Diff plugin for Nautilus
Summary(pl.UTF-8):	Wtyczka diffa dla Nautilusa
%define     realname    gdiff-ext
Name:		nautilus-%{realname}
Version:	0.2.4
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:    http://dl.sourceforge.net/diff-ext/%{realname}-%{version}.tar.bz2
# Source0-md5:	19d7c6eff7d3eb6ba993a1eb91a09563
Patch0:     %{name}-typo.patch
URL:		http://diff-ext.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:  automake
BuildRequires:  GConf2-devel >= 2.20.1
BuildRequires:  gtk+2-devel >= 2.12.8
BuildRequires:  intltool
BuildRequires:  nautilus-devel >= 2.20.0
BuildRequires:  libtool
Requires:	    diffutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gdiff-ext is context menu extension for GNOME's Nautilus file manager.
Gdiff-ext extends Nautilus context menu with commands to compare or
merge selected file(s) and to remember selected file for the future
compare or merge operation.

%description -l pl.UTF-8
Gdiff-ext jest rozszerzeniem menu kontekstowego dla zarządcy plików
Nautilus GNOME-a. Gdiff-ext rozszerza menu kontekstowe Nautilusa
komendami do porównywania albo scalania plików i zapamiętuje wybrane
pliki dla przyszłych porównań i scaleń.

%prep
%setup -q -n %{realname}-%{version}
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{realname}.schemas

%postun
%gconf_schema_uninstall

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_sysconfdir}/gconf/schemas/diff-ext.schemas
%attr(755,root,root) %{_bindir}/*
%{_libdir}/nautilus/extensions-1.0/libdiff-ext.so
%{_desktopdir}/diff-ext.desktop
%{_datadir}/%{realname}
%{_iconsdir}/hicolor/16x16/apps/de.png
