%define name    ecap
%define version 0.0.3
%define release %mkrel 3
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    eCAP library
License:    BSD
Group:      Networking/Other
URL:        http://www.e-cap.org/
Source:     http://www.measurement-factory.com/tmp/ecap/libecap-%{version}.tar.gz
BuildRequires:  kernel-headers
%if %mdkversion < 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}
%endif

%description
eCAP is a software interface that allows a network application, such as an 
HTTP proxy or an ICAP server, to outsource content analysis and adaptation 
to a loadable module. For each applicable protocol message being 
processed, an eCAP-enabled application supplies the message details to the 
adaptation module and gets back an adapted message or a "not interested" 
response. These exchanges often include message bodies.

%package -n     %{libname}
Summary:        Main library for dssl
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
DSSL library is a network caputre and SSL decryption toolkit useful for snort and other SSL aware
software.


%package        -n     %{develname}
Summary:        Header files for the dssl library
Group:          Development/C
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description    -n %{develname}
DSSL library is a network caputre and SSL decryption toolkit useful for snort and other SSL aware
software.  These are .h files.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%prep
%setup -q -n libecap-%{version}

#export LIBS=-lpcap 
%configure2_5x --enable-shared --enable-std-include

%build
%make
%install
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libecap.so.%{major}*


%files  -n %{develname}
%defattr(-,root,root)
%{_includedir}/libecap/*
%{_libdir}/libecap.so
%{_libdir}/libecap.a
%{_libdir}/libecap.la

