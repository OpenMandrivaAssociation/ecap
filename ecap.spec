%define major 2
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Name:		ecap
Version:	0.2.0
Release:	2
Summary:	eCAP library
License:	BSD
Group:		Networking/Other
URL:		http://www.e-cap.org/
Source0:	http://www.measurement-factory.com/tmp/ecap/libecap-%{version}.tar.gz
BuildRequires:	kernel-headers

%description
eCAP is a software interface that allows a network application, such as an 
HTTP proxy or an ICAP server, to outsource content analysis and adaptation 
to a loadable module. For each applicable protocol message being 
processed, an eCAP-enabled application supplies the message details to the 
adaptation module and gets back an adapted message or a "not interested" 
response. These exchanges often include message bodies.

%package -n %{libname}
Summary:	Main library for dssl
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
DSSL library is a network caputre and SSL decryption toolkit useful for
snort and other SSL aware software.

%package -n %{develname}
Summary:	Header files for the dssl library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description    -n %{develname}
DSSL library is a network caputre and SSL decryption toolkit useful for
snort and other SSL aware software.  These are .h files.

%prep
%setup -qn libecap-%{version}

%build
%configure2_5x \
	--enable-shared \
	--enable-std-include

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/libecap.la

%files -n %{libname}
%doc LICENSE
%{_libdir}/libecap.so.%{major}*

%files  -n %{develname}
%{_includedir}/libecap/*
%{_libdir}/libecap.so
%{_libdir}/libecap.a
%{_libdir}/pkgconfig/libecap.pc



%changelog
* Sat Feb 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.0-1
+ Revision: 772536
- fixed files list
- new version 0.2.0
- new major 2

* Sat Feb 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.3-4
+ Revision: 772531
- rebuild
- cleaned up spec

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-3
+ Revision: 664117
- mass rebuild

* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.0.3-2
+ Revision: 647069
- Rebuild

* Wed Dec 29 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.0.3-1mdv2011.0
+ Revision: 625816
- 0.0.3

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-5mdv2011.0
+ Revision: 605094
- rebuild

* Sat Mar 20 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.0.2-4mdv2010.1
+ Revision: 525373
- Bump release

* Fri Mar 19 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.2-3mdv2010.1
+ Revision: 525320
- bump release
- add the LICENSE

* Thu Feb 25 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 510857
- Fix lib requires

* Wed Feb 24 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.0.2-1mdv2010.1
+ Revision: 510531
- import ecap


