%define major	2
%define libname	%mklibname %{name}  %{major}
%define devname	%mklibname %{name} -d

Summary:	eCAP library
Name:		ecap
Version:	0.2.0
Release:	9
License:	BSD
Group:		Networking/Other
Url:		http://www.e-cap.org/
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

%package -n %{devname}
Summary:	Header files for the dssl library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description    -n %{devname}
DSSL library is a network caputre and SSL decryption toolkit useful for
snort and other SSL aware software.  These are .h files.

%prep
%setup -qn libecap-%{version}

%build
%configure2_5x \
	--disable-static \
	--enable-shared \
	--enable-std-include

%make

%install
%makeinstall_std

%files -n %{libname}
%doc LICENSE
%{_libdir}/libecap.so.%{major}*

%files  -n %{devname}
%{_includedir}/libecap/*
%{_libdir}/libecap.so
%{_libdir}/pkgconfig/libecap.pc

