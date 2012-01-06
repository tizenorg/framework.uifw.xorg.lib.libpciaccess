
Name:       libpciaccess
Summary:    PCI access library
Version:    0.12.0
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  zlib-devel


%description
Generic PCI access library


%package devel
Summary:    PCI access library development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Generic PCI access library development package


%prep
%setup -q -n %{name}-%{version}


%build

%configure --disable-static \
    --with-pciids-path=%{_prefix}/share/misc --with-zlib \

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.10.8


%files devel
%defattr(-,root,root,-)
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc

