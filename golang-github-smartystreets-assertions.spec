# https://github.com/smartystreets/assertions
%global goipath         github.com/smartystreets/assertions
%global commit          b2de0cb4f26d0705483a2f495d89896d0b808573

%global common_description %{expand:
Package assertions contains the implementations for all assertions which are 
referenced in goconvey's convey package 
(github.com/smartystreets/goconvey/convey) and gunit 
(github.com/smartystreets/gunit) for use with the So(...) method. They can 
also be used in traditional Go test functions and even in applications.}

%gometa

Name:           %{goname}
Version:        1.8.3
Release:        1%{?dist}
Summary:        Fluent assertion-style functions
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}


%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.md
%doc README.md CONTRIBUTING.md


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.8.3-1.20181006gitb2de0cb
- Bump to commit b2de0cb4f26d0705483a2f495d89896d0b808573
- Update with new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.8.git287b434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.7.git287b434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.6.git287b434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.5.git287b434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-0.4.git287b434
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.6.0-0.3.git287b434
- Polish the spec file
  related: #1250509

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.2.git287b434
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 1.6.0-0.1.git287b434
- Bump to upstream 287b4346dc4e71a038c346375a9d572453bc469b
  Polish the spec file
  related: #1250509

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git4727d76
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git4727d76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git4727d76
- Just rebuild
  related: #1250509

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git4727d76
- internal packages are not provided but are needed for building
  related: #1250509
  resolves: #1255155

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git4727d76
- internal packages can not be provided since go-1.5
  related: #1250509

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git4727d76
- Update spec file to spec-2.0
  resolves: #1250509

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4727d76
- First package for Fedora
  resolves: #1214816

