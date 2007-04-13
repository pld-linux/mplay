%include	/usr/lib/rpm/macros.perl
Summary:	Console based frontend to MPlayer
Summary(pl.UTF-8):	Konsolowa nakładka na MPlayera
Name:		mplay
Version:	0.80
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplay/%{name}-%{version}.tar.gz
# Source0-md5:	60487eeedbeb3444cab24e2783cee052
Source1:	%{name}.desktop
URL:		http://mplay.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplay is a front-end to MPlayer. It extends its functions in several
significant ways. It:
- keeps playlist
- provides essential status information
- includes a progress bar
- remembers the position within the track last played before quitting
- provides basic mixer functions

%description -l pl.UTF-8
mplay jest nakładką na MPlayera rozszerzającą jego funkcjonalność na
kila sposobów:
- zarządza listami odtwarzania
- dostarcza istotnych informacji na temat statusu
- wyświetla belkę postępu
- zapamiętuje pozycję ścieżki, która była odtwarzana przed wyjściem
- dostarcza podstawowych funkcji miksera

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

sed -i "s#/local/share/#/share/#g" mplay

install mplay $RPM_BUILD_ROOT%{_bindir}
install help/help_* $RPM_BUILD_ROOT%{_datadir}/%{name}
install help/mplay.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
