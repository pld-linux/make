Summary:	GNU Make
Summary(de):	GNU Make
Summary(fr):	L'utilitaire make de GNU
Summary(pl):	GNU Make
Summary(tr):	GNU Make
Name:		make
Version:	3.79.1
Release:	10
Epoch:		1
License:	GPL
Group:		Development/Building
Group(de):	Entwicklung/Bauen
Group(pl):	Programowanie/Budowanie
Source0:	ftp://prep.ai.mit.edu/pub/gnu/make/%{name}-%{version}.tar.gz
Source1:	%{name}.1.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-noclock_gettime.patch
Patch2:		%{name}-pl.po.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

The GNU make tool should be installed on your system because it is
commonly used to simplify the process of installing programs.

%description -l de
Das MAKE-Programm dient zur Koordination der Kompilierung und zum
Linken eines Satzes von Quellen in ein Programm, wobei nur die
erforderlichen Komponenten neu kompiliert werden, so da� der
Entwickler eine Menge Zeit spart. Aber damit sind die F�higkeiten von
MAKE noch lange nicht ersch�pft
- lesen Sie die Info-Dokumente.

%description -l fr
make sert � coordonner la compilation et l'�dition de liens d'un
ensemble de sources pour produire un programme, ne recompilant que ce
qui est n�cessaire et �conomisant ainsi beaucoup de temps. En fait,
make peut faire beaucoup plus -- voir les docs info.

%description -l pl
Make jest u�ywany do automatyzacji proces�w kompilowania kodu
�r�d�owego i konsolidacji kodu program�w wykonuj�c tylko te czynno�ci
kt�re s� potrzebne w razie modyfikacji plik�w przetwarzanych przez
make oszcz�dzaj�c tym samym czas. Make mo�e wykonywa� o wiele wi�cej
r�nych typ�w operacji zwi�zanych z przedtwarzaniem wsadowym. Pe�en
opis make znale�� mo�na na�stronach info ("info make").

%description -l tr
Bu program kaynak kodlar�n�n derlenmesini ve ba�lanmas�n� koordine
etmek i�in kullan�l�r. Sadece gerekli olan programlar� tekrar
derleyerek zaman yitirilmesini �nler.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm missing
aclocal
autoconf
automake -a -c -i
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/{,pl}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/make.1

gzip -9nf NEWS README

%find_lang %{name}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/make.info*
