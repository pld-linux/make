Summary:	GNU Make
Summary(de):	GNU Make
Summary(fr):	L'utilitaire make de GNU
Summary(pl):	GNU Make
Summary(tr):	GNU Make
Name:		make
Version:	3.77
Release:	7
Copyright:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source:		ftp://prep.ai.mit.edu/pub/gnu/make/%{name}-%{version}.tar.gz
Patch0:		make-info.patch
Patch1:		make-fixes.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
The program make is used to coordinate the compilation and linking of a set
of sources into a program, recompiling only what is necessary, thus saving a
developer a lot of time. In fact, make can do a lot more - read the info
docs.

%description -l de
Das MAKE-Programm dient zur Koordination der Kompilierung und zum Linken
eines Satzes von Quellen in ein Programm, wobei nur die erforderlichen
Komponenten neu kompiliert werden, so da� der Entwickler eine Menge Zeit
spart. Aber damit sind die F�higkeiten von MAKE noch lange nicht ersch�pft -
lesen Sie die Info-Dokumente.

%description -l fr
make sert � coordonner la compilation et l'�dition de liens d'un ensemble de
sources pour produire un programme, ne recompilant que ce qui est n�cessaire
et �conomisant ainsi beaucoup de temps. En fait, make peut faire beaucoup
plus -- voir les docs info.

%description -l tr
Bu program kaynak kodlar�n�n derlenmesini ve ba�lanmas�n� koordine etmek
i�in kullan�l�r. Sadece gerekli olan programlar� tekrar derleyerek zaman
yitirilmesini �nler.

%description -l pl
Make jest u�ywany do automatyzacji proces�w kompilowania kodu �r�d�owego i
konsolidacji kodu program�w wykonuj�c tylko te czynno�ci kt�re s� potrzebne
w razie modyfikacji plik�w przetwarzanych przez make oszcz�dzaj�c tym samym
czas. Make mo�e wykonywa� o wiele wi�cej r�nych typ�w operacji zwi�zanych z
przedtwarzaniem wsadowym. Pe�en opis make znale�� mo�na na�stronach info
("info make").

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/make.info*,%{_mandir}/man1/*} \
	NEWS README

%post
/sbin/install-info %{_infodir}/make.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/make.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_infodir}/make.info*

%changelog
* Thu May 27 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.77-7]
- based on RH spec,
- spec rewrited by PLD team.
