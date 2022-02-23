Summary:	QNapi - Movie Subtitle Downloader
Summary(pl.UTF-8):	QNapi - program pobierający napisy do filmów
Name:		qnapi
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	https://github.com/QNapi/qnapi/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5280a524031e31baa94ded730cff0bdd
Patch0:		qt-5.15.patch
URL:		http://qnapi.github.io/
BuildRequires:	Qt5Gui-devel >= 4.3.0
BuildRequires:	Qt5Network-devel >= 4.3.0
BuildRequires:	Qt5Xml-devel >= 4.3.0
BuildRequires:	libmediainfo-devel
BuildRequires:	qt5-build >= 4.3.0
BuildRequires:	qt5-qmake >= 4.3.0
Requires:	p7zip
Obsoletes:	qnapi-kde4 < 0.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QNapi are unofficial and free clone of NAPI-PROJEKT written for Linux
(and other OS) users, for which there is no official NAPI-PROJEKT
client. This program has functionality similar to the original client
(adding subtitles, sending bug reports etc.), thus it helps in
increasing NAPI database.

%description -l pl.UTF-8
QNapi jest nieoficjalnym, wolnym klonem programu NAPI-PROJEKT,
napisanym z myślą o użytkownikach Linuksa oraz innych systemów
operacyjnych, pod które oryginalny NAPI-PROJEKT nie jest dostępny.
Program ma funkcjonalność zbliżoną do oryginalnego klienta (m.in.
dodawanie napisów, zgłaszanie raportów o błędach), przez co pozwala
zwiększyć rozmiar bazy NAPI.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt5
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ChangeLog README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/*x*/apps/%{name}*.png
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.*
%lang(it) %{_mandir}/it/man1/%{name}.*
%lang(pl) %{_mandir}/pl/man1/%{name}.*
