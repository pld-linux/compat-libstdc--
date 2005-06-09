Summary:	Old versions of GNU C++ library
Summary(pl):	Stare wersje bibliotek GNU C++
Name:		compat-libstdc++
Version:	3.3
Release:	5
License:	GPL
Group:		Libraries
#Source0:	libstdc++-compat.tar.gz
Source0:	http://pld-nptl.ds14.agh.edu.pl/libstdc++-compat.tar.gz
# Source0-md5:	98ab37235f8cf0d20251716dabd40690
BuildRequires:	rpmbuild(macros) >= 1.213
# only 3.3 on %{x8664}, so not for Ac
ExclusiveArch:	%{ix86} alpha ppc sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNU implementation of the standard C++ libraries, along
with additional GNU tools. This package includes the compatibility
shared libraries necessary to run some old C++ applications.

%description -l de
Dies ist die GNU-Implementierung der Standard-C++-Libraries mit
weiteren GNU-Tools. Dieses Paket enthält die zum Ausführen von
C++-Anwendungen erforderlichen gemeinsam genutzten Libraries.

%description -l fr
Ceci est l'implémentation GNU des librairies C++ standard, ainsi que
des outils GNU supplémentaires. Ce package comprend les librairies
partagées nécessaires à l'exécution d'application C++.

%description -l pl
Pakiet ten zawiera biblioteki bêd±ce implementacj± standardowych
bibliotek C++, znajduj± siê w nim stare biblioteki dynamiczne
niezbêdne do uruchomienia niektórych starych aplikacji C++.

%description -l tr
Bu paket, standart C++ kitaplýklarýnýn GNU gerçeklemesidir ve C++
uygulamalarýnýn koþturulmasý için gerekli kitaplýklarý içerir.

%package -n compat-libg++-2.7
Summary:	Old version of GNU C++ library - libg++ 2.7.x
Summary(pl):	Stara wersja biblioteki GNU C++ - libg++ 2.7.x
Version:	2.7.2.8
Group:		Libraries
Obsoletes:	libg++
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description -n compat-libg++-2.7
Old, compatibility version of GNU C++ library - libg++ 2.7.x (from gcc
2.7.x), needed to run some old C++ applications.

%description -n compat-libg++-2.7 -l pl
Stara wersja biblioteki GNU C++ - libg++ 2.7.x (z gcc 2.7.x) potrzebna
dla kompatybilno¶ci z niektórymi starymi programami w C++.

%package 2.7
Summary:	Old version of GNU C++ library - 2.7.x
Summary(pl):	Stara wersja biblioteki GNU C++ - 2.7.x
Version:	2.7.2.8
Group:		Libraries
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 2.7
Old, compatibility version of GNU C++ library - libstdc++ 2.7.x (from
gcc 2.7.x), needed to run some old C++ applications.

%description 2.7 -l pl
Stara wersja biblioteki GNU C++ - libstdc++ 2.7.x (z gcc 2.7.x)
potrzebna dla kompatybilno¶ci z niektórymi starymi programami w C++.

%package 2.8
Summary:	Old version of GNU C++ library - 2.8
Summary(pl):	Stara wersja biblioteki GNU C++ - 2.8
Version:	2.8.0
Group:		Libraries
%ifarch ppc
Provides:	libstdc++.so.27
%endif
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 2.8
Old, compatibility version of GNU C++ library - libstdc++ 2.8.0 (from
gcc 2.8.x), needed to run some old C++ applications.

%description 2.8 -l pl
Stara wersja biblioteki GNU C++ - libstdc++ 2.8.0 (z gcc 2.8.x)
potrzebna dla kompatybilno¶ci z niektórymi starymi programami w C++.

%package 2.9
Summary:	Old version of GNU C++ library - 2.9
Summary(pl):	Stara wersja biblioteki GNU C++ - 2.9
Version:	2.9.0
Group:		Libraries
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 2.9
Old, compatibility version of GNU C++ library - libstdc++ 2.9.0 (from
egcs 1.x-2.9x?), needed to run some old C++ applications.

%description 2.9 -l pl
Stara wersja biblioteki GNU C++ - libstdc++ 2.9.0 (z egcs 1.x-2.9x?)
potrzebna dla kompatybilno¶ci z niektórymi starymi programami w C++.

%package 2.10
Summary:	Old version of GNU C++ library - 2.10
Summary(pl):	Stara wersja biblioteki GNU C++ - 2.10
Version:	2.10.0
Group:		Libraries
%ifarch ppc
Provides:	libstdc++-libc6.1-2.so.3
%endif
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 2.10
Old, compatibility version of GNU C++ library - libstdc++ 2.10.0 (from
gcc 2.95.x), needed to run some old C++ applications.

%description 2.10 -l pl
Stara wersja biblioteki GNU C++ - libstdc++ 2.10.0 (z gcc 2.95.x)
potrzebna dla kompatybilno¶ci z niektórymi starymi programami w C++.

%package 3.0
Summary:	Old version of GNU C++ library - gcc 3.0
Summary(pl):	Stara wersja biblioteki GNU C++ - gcc 3.0
%ifarch alpha
Version:	3.0.2
%else
Version:	3.0.4
%endif
Group:		Libraries
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 3.0
Old, compatibility version of GNU C++ library - from gcc 3.0.x, needed
to run some old C++ applications.

%description 3.0 -l pl
Stara wersja biblioteki GNU C++ - z gcc 3.0.x, potrzebna dla
kompatybilno¶ci z niektórymi starymi programami w C++.

%package 3.1
Summary:	Old version of GNU C++ library - gcc 3.1
Summary(pl):	Stara wersja biblioteki GNU C++ - gcc 3.1
Version:	3.1.1
Group:		Libraries
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 3.1
Old, compatibility version of GNU C++ library - from gcc 3.1.x, needed
to run some old C++ applications.

%description 3.1 -l pl
Stara wersja biblioteki GNU C++ - z gcc 3.1.x, potrzebna dla
kompatybilno¶ci z niektórymi starymi programami w C++.

%package 3.3
Summary:	Old version of GNU C++ library - gcc 3.3
Summary(pl):	Stara wersja biblioteki GNU C++ - gcc 3.3
Version:	3.3.5
Group:		Libraries
Conflicts:	compat-libstdc++
Conflicts:	libstdc++-compat

%description 3.3
Old, compatibility version of GNU C++ library - from gcc 3.3.5, needed
to run some old C++ applications.

%description 3.3 -l pl
Stara wersja biblioteki GNU C++ - z gcc 3.3.5, potrzebna dla
kompatybilno¶ci z niektórymi starymi programami w C++.


%prep
%setup -q -n libstdc++-compat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%ifarch alpha
cp -a alpha/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{x8664}
cp -a amd64/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch sparc
cp -a sparc/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{ix86}
cp -a i386/* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch ppc
cp -a ppc/* $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n compat-libg++-2.7 -p /sbin/ldconfig
%postun	-n compat-libg++-2.7 -p /sbin/ldconfig

%post	2.7 -p /sbin/ldconfig
%postun	2.7 -p /sbin/ldconfig

%post	2.8 -p /sbin/ldconfig
%postun	2.8 -p /sbin/ldconfig

%post	2.9 -p /sbin/ldconfig
%postun	2.9 -p /sbin/ldconfig

%post	2.10 -p /sbin/ldconfig
%postun	2.10 -p /sbin/ldconfig

%post	3.0 -p /sbin/ldconfig
%postun	3.0 -p /sbin/ldconfig

%post	3.1 -p /sbin/ldconfig
%postun	3.1 -p /sbin/ldconfig

%post	3.3 -p /sbin/ldconfig
%postun	3.3 -p /sbin/ldconfig

%ifarch alpha %{ix86}
%files -n compat-libg++-2.7
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libg++.so.2.7.2.8
%endif

%ifarch alpha %{ix86}
%files 2.7
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.2.7.2.8
%endif

%ifarch alpha %{ix86} ppc sparc
%files 2.8
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.2.8.0
%ifarch ppc
%attr(755,root,root) %{_libdir}/libstdc++.so.27
%endif
%endif

%ifarch alpha %{ix86} sparc
%files 2.9
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++-2-libc6.1-1-2.9.0.so
%ifarch alpha sparc
%attr(755,root,root) %{_libdir}/libstdc++.so.2.9.0
%endif
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/libstdc++.so.2.9.dummy
%endif
%endif

%ifarch %{ix86} ppc
%files 2.10
%defattr(644,root,root,755)
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/libstdc++-3-libc6.2-2-2.10.0.so
%endif 
%ifarch ppc
%attr(755,root,root) %{_libdir}/libstdc++-3-libc6.1-2-2.10.0.so
%attr(755,root,root) %{_libdir}/libstdc++-libc6.1-2.so.3
%endif
%endif

%ifarch alpha %{ix86} sparc
%files 3.0
%defattr(644,root,root,755)
%ifarch alpha
%attr(755,root,root) %{_libdir}/libstdc++.so.3.0.2
%endif
%ifarch %{ix86} sparc
%attr(755,root,root) %{_libdir}/libstdc++.so.3.0.4
%endif
%endif

%ifarch %{ix86} ppc
%files 3.1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.4.0.1
%endif

# not for Ac
%if 0
%ifarch alpha %{x8664} %{ix86} ppc sparc
%files 3.3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libstdc++.so.5.0.7
%endif
%endif
