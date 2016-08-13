Name:           vdr-plex
Version:        0.4.0
Release:        2%{?dist}
Summary:        A Plex Client for the VDR

Group:          Applications/Multimedia
License:        GPLv2
URL:            http://projects.vdr-developer.org/projects/plg-plex
SOURCE:         https://projects.vdr-developer.org/git/vdr-plugin-plex.git/snapshot/vdr-plugin-plex-%{version}.tar.bz2

BuildRequires:  vdr-devel >= 2.0.0
BuildRequires:  openssl-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  pcre-devel
BuildRequires:  poco-devel >= 1.7.3-5
BuildRequires:  libskindesignerapi-devel >= 1.1.4
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
Plays Videos directly in the VDR, via softhddevice, full-featured not tested.
Browse your plex media server, and play your media.
Control via Plex for Android/IOS/Web, play, pause, stop, seeking
Cast Vimeo, Youtube, Apple-Trailers, and many other Plexchannels to your VDR.

%prep
%setup -qn vdr-plugin-plex-%{version}

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Fri Aug 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-2
- fixed license type
- switched from git to stable release numbering

* Tue Jun 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.20160626gitd005101
- rebuild for new git version

* Thu Mar 31 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1.20160330giteef71c6
- rebuild for new git version

* Mon Feb 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-1.20160221git6b8c8ae
- rebuild for new git version

* Sat Jun 27 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-1.20150627gitb6a8493
- rebuild for new git version

* Sat Feb 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-1.20150213gite412257
- Initial build