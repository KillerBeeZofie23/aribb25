Name:           aribb25
Version:        0.2.7
Release:        1%{?dist}
Summary:        Basic implementation of the ARIB STD-B25 public standard
License:        ISC Licence
URL:            http://www.videolan.org/

Source0:        https://download.videolan.org/pub/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(libpcsclite)

%description
This implementation currently only allows playback of ARIB scrambled streams.

With the end of analog TV in Japan in July 2011 a wish for cheap Digital TV
receivers emerged. Although, the volontary introduced complexity in the ARIB
standard makes it really hard to understand, induces higher development costs
for device manufacturers and then nullifies the chances of having low cost
receivers on the market.

For that reason, this library gathers most of the necessary specification into a
comprehensible code that can be used as a starting point.

The Conditional Access system (CA) accordingly to the associated B-CAS Card will
decrypt TS streams using the ECM table 0x82 and EMM table 0x84.
EMM table 0x85 messages processing are to be done.

Conditional Access Cards can be read through any ISO-7816
compliant IC card reader.

Known and working card readers are:
 * Hitachi / Maxell HX-520UJ (Windows Only)
 * NTT SCR-3310 eTax reader

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fr %{buildroot}%{_docdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENCE
%doc README.*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jul 22 2016 Simone Caronni <negativo17@gmail.com> - 0.2.7-1
- First build.
