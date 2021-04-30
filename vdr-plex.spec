Name:           vdr-plex
Version:        0.4.0
Release:        22%{?dist}
Summary:        A Plex Client for the VDR
License:        GPLv2
URL:            http://projects.vdr-developer.org/projects/plg-plex
Source:         https://projects.vdr-developer.org/git/vdr-plugin-plex.git/snapshot/vdr-plugin-plex-%{version}.tar.bz2
Patch0:         %{name}-namespace.patch

BuildRequires:  gcc-c++
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
%autosetup -p1 -n vdr-plugin-plex-%{version}

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Mon Apr 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-22
- Rebuilt for new VDR API version

* Sat Apr 24 2021 Leigh Scott <leigh123linux@gmail.com> - 0.4.0-21
- Rebuilt for removed libstdc++ symbol (#1937698)

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-19
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-18
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-17
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 leigh123linux <leigh123linux@googlemail.com> - 0.4.0-15
- Rebuild for new poco version

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-12
- Rebuilt for new VDR API version 2.4.1

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-11
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-9
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.4.0-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-6
- Rebuilt for vdr-2.4.0

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-4
- add %%{name}-namespace.patch.patch

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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
