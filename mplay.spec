%include	/usr/lib/rpm/macros.perl
Summary:	Console based frontend to MPlayer
Summary(pl):	Konsolowa nak³adka na MPlayera
Name:		mplay
Version:	0.42
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplay/%{name}-%{version}.tar.gz
# Source0-md5:	de77b6ca631c64e52c0b1c6b67636796
Patch0:		%{name}-install.patch
URL:		http://mplay.sourceforge.net/
BuildRequires:	rpm-perlprov
BuildRequires:	sed
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
%patch0 -p1

%build
./install

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

sed -e "s#/share/local/#/share/#g" mplay > mplay.tmp
mv -f mplay.tmp mplay

install mplay $RPM_BUILD_ROOT%{_bindir}
install help_* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
