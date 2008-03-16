Summary:	QNapi - Movie Subtitle Downloader
Summary(pl.UTF-8):	QNapi - program pobierający napisy do filmów
Name:		qnapi
Version:	0.1.3
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/qnapi/%{name}-%{version}.tar.gz
# Source0-md5:	ce22cb608228868791c32e8dafe3be10
Source1:	%{name}-konqueror.desktop
URL:		http://krzemin.iglu.cz/qnapi/
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	QtNetwork-devel >= 4.3.0
BuildRequires:	qt4-build >= 4.3.0
BuildRequires:	qt4-qmake >= 4.3.0
Requires:	p7zip
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

%package konqueror
Summary:	Konqueror actions for QNapi
Summary(pl.UTF-8):	Akcje QNapi dla Konquerora
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	konqueror

%description konqueror
QNapi actions on media files for Konqueror.

%description konqueror -l pl.UTF-8
Ten pakiet dodaje do Konquerora akcje QNapi na plikach
multimedialnych.

%package dolphin
Summary:	dolphin actions for QNapi
Summary(pl.UTF-8):	Akcje QNapi dla Dolphina
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	kde-dolphin

%description dolphin
QNapi actions on media files for Dolphin.

%description dolphin -l pl.UTF-8
Ten pakiet dodaje do Dolphina akcje QNapi na plikach multimedialnych.

%prep
%setup -q

%build
qmake-qt4 -unix -o Makefile %{name}.pro
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install qnapi $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install doc/manpage $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}-48.png $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}-128.png $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}-512.png $RPM_BUILD_ROOT%{_iconsdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install doc/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus
install -d $RPM_BUILD_ROOT%{_datadir}/apps/dolphin/servicemenus
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/apps/dolphin/servicemenus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ChangeLog doc/README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_iconsdir}/%{name}*.png
%{_desktopdir}/%{name}.desktop

%files konqueror
%defattr(644,root,root,755)
%{_datadir}/apps/konqueror/servicemenus/%{name}*.desktop

%files dolphin
%defattr(644,root,root,755)
%{_datadir}/apps/dolphin/servicemenus/%{name}*.desktop
