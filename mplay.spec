%include	/usr/lib/rpm/macros.perl
Summary:	Console based frontend to MPlayer
Summary(pl):	Konsolowa nak�adka na MPlayera
Name:		mplay
Version:	0.68
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplay/%{name}-%{version}.tar.gz
# Source0-md5:	c2f5ce07352ccf1b7effecb28a7f4fd1
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

%description -l pl
mplay jest nak�adk� na MPlayera rozszerzaj�c� jego funkcjonalno�� na
kila sposob�w:
- zarz�dza listami odtwarzania
- dostarcza istotnych informacji na temat statusu
- wy�wietla belk� post�pu
- zapami�tuje pozycj� �cie�ki, kt�ra by�a odtwarzana przed wyj�ciem
- dostarcza podstawowych funkcji miksera

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man1}

sed -e "s#/local/share/#/share/#g" mplay > mplay.tmp
mv -f mplay.tmp mplay

install mplay $RPM_BUILD_ROOT%{_bindir}
install help/help_* $RPM_BUILD_ROOT%{_datadir}/%{name}
install help/mplay.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_mandir}/man1/*
