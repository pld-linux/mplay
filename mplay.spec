%include	/usr/lib/rpm/macros.perl
Summary:	Console based frontend to MPlayer
Summary(pl):	Konsolowa nak³adka na MPlayera
Name:		mplay
Version:	0.53
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplay/%{name}-%{version}.tar.gz
# Source0-md5:	00c8230d5ccce61e2019bc924f0ab13c
Source1:	%{name}.desktop
URL:		http://mplay.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires:	mplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_desktopdir	%{_applnkdir}/Multimedia

%description
mplay is a front-end to MPlayer. It extends its functions in several
significant ways. It:
- keeps playlist
- provides essential status information
- includes a progress bar
- remembers the position within the track last played before quitting
- provides basic mixer functions

%description -l pl
mplay jest nak³adk± na MPlayera rozszerzaj±c± jego funkcjonalno¶æ na
kila sposobów:
- zarz±dza listami odtwarzania
- dostarcza istotnych informacji na temat statusu
- wy¶wietla belkê postêpu
- zapamiêtuje pozycjê ¶cie¿ki, która by³a odtwarzana przed wyj¶ciem
- dostarcza podstawowych funkcji miksera

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir}}

sed -e "s#/local/share/#/share/#g" mplay > mplay.tmp
mv -f mplay.tmp mplay

install mplay $RPM_BUILD_ROOT%{_bindir}
install help/help_* $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
