# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 43
%global vdr_version 2.7.6
%elif 0%{?fedora} == 42
%global vdr_version 2.7.4
%else
%global vdr_version 2.6.9
%endif

Name:           vdr-plex
Version:        0.4.0
Release:        46%{?dist}
Summary:        A Plex Client for the VDR
License:        GPL-2.0-only
URL:            https://github.com/chriszero/vdr-plugin-plex
Source:         %url/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-namespace.patch
Patch1:         0002-plex-Removal-of-deprecated-interface-functions.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
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
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC -DPOCO_UNBUNDLED" all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Sat Jun 21 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-46
- Rebuilt for new VDR API version 2.7.6

* Mon Apr 14 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-45
- Rebuilt for new VDR API version 2.7.5

* Sun Mar 16 2025 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-44
- Rebuilt for new VDR API version 2.7.4

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-42
- Rebuilt for new VDR API version 2.7.3

* Tue Oct 01 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-41
- Add 0002-plex-Removal-of-deprecated-interface-functions.patch for vdr-2.7.x

* Fri Jul 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-40
- Rebuilt for new VDR API version 2.6.9

* Sun Apr 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-39
- Rebuilt for new VDR API version

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-37
- Rebuilt for new VDR API version

* Tue Jan 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-36
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.4.0-34
- rebuilt

* Sun Dec 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-33
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-32
- Rebuilt for new VDR API version

* Wed Aug 24 2022 Leigh Scott <leigh123linux@gmail.com> - 0.4.0-31
- Rebuilt for new poco

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Fri Aug 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-29
- Update to new github address

* Wed May 11 2022 Sérgio Basto <sergio@serjux.com> - 0.4.0-28
- Poco package is fixed, no need set flag POCO_UNBUNDLED

* Tue Apr 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-27
- Set flag POCO_UNBUNDLED

* Mon Apr 11 2022 Sérgio Basto <sergio@serjux.com> - 0.4.0-26
- Rebuilt for VDR 2.6.x

* Sat Feb 05 2022 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-25
- Rebuilt for new VDR API version

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-24
- Rebuilt for new VDR API version

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

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
