#define gitdate 20111109
#define gitrev  a0a53a67c91c698007dcac3e7aba27c999c4f6ed

Name:           libpciaccess
Version:        0.13.1
Release:        1
Summary:        PCI access library

Group:          System Environment/Libraries
License:        MIT
URL:            http://gitweb.freedesktop.org/?p=xorg/lib/libpciaccess.git

Source0:	%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool pkgconfig xorg-x11-xutils-dev
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  zlib-devel

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for libpciaccess.

%prep
%setup -q

%build
# autoreconf -v --install
%reconfigure --disable-static \
           --with-pciids-path=%{_prefix}/share/misc --with-zlib \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.11.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc
