#
Summary:	QNapi - Movie Subtitle Downloader
Summary(pl.UTF-8):	QNapi - program pobierający napisy do filmów
Name:		qnapi
Version:	0.1.2
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://krzemin.iglu.cz/qnapi/%{name}-%{version}.tar.gz
# Source0-md5:	4451928c89a9d92ca53d849793b55b0a
URL:		http://krzemin.iglu.cz/qnapi/
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	QtNetwork-devel >= 4.3.0
BuildRequires:	qt4-build >= 4.3.0
BuildRequires:	qt4-qmake >= 4.3.0
Requires:	p7zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QNapi are unofficial and free clone of NAPI-PROJEKT written for Linux
users.

%description -l pl.UTF-8
QNapi jest nieoficjalnym, wolnym klonem programu NAPI-PROJEKT,
napisanym z myślą o użytkownikach Linuksa oraz innych systemów
operacyjnych, pod które oryginalny NAPI-PROJEKT nie jest dostępny.
Program ma funkcjonalność zbliżoną do oryginalnego klienta (m.in.
dodawanie napisów, zgłaszanie raportów o błędach), przez co
pozwala zwiększyć rozmiar bazy NAPI.

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
install manpage $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install -d $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}
install src/%{name}_44x44.png $RPM_BUILD_ROOT%{_iconsdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_iconsdir}/%{name}*.png
%{_desktopdir}/%{name}.desktop
