Summary:	GNU Make
Summary(de):	GNU Make
Summary(fr):	L'utilitaire make de GNU
Summary(pl):	GNU Make
Summary(tr):	GNU Make
Name:		make
Version:	3.77
Release:	4
Copyright:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source:		ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Patch:		make-info.patch
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
Komponenten neu kompiliert werden, so daß der Entwickler eine Menge Zeit
spart. Aber damit sind die Fähigkeiten von MAKE noch lange nicht erschöpft -
lesen Sie die Info-Dokumente.

%description -l fr
make sert à coordonner la compilation et l'édition de liens d'un ensemble de
sources pour produire un programme, ne recompilant que ce qui est nécessaire
et économisant ainsi beaucoup de temps. En fait, make peut faire beaucoup
plus -- voir les docs info.

%description -l tr
Bu program kaynak kodlarýnýn derlenmesini ve baðlanmasýný koordine etmek
için kullanýlýr. Sadece gerekli olan programlarý tekrar derleyerek zaman
yitirilmesini önler.

%description -l pl
Make jest u¿ywany do automatyzacji procesów kompilowania kodu ¼ród³owego i
konsolidacji kodu programów wykonuj±c tylko te czynno¶ci które s± potrzebne
w razie modyfikacji plików przetwarzanych przez make oszczêdzaj±c tym samym
czas. Make mo¿e wykonywaæ o wiele wiêcej ró¿nych typów operacji zwi±zanych z
przedtwarzaniem wsadowym. Pe³en opis make znale¼æ mo¿na na stronach info
("info make").

%prep
%setup -q
%patch -p1

%build
./configure --prefix=/usr
make "CFLAGS=$RPM_OPT_FLAGS"

%install
rm -f $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/man/man1

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/make

gzip -9nf $RPM_BUILD_ROOT/usr/{info/make.info*,man/man1/*}

%post
/sbin/install-info /usr/info/make.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/make.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) /usr/bin/*

/usr/man/man1/*
/usr/info/make.info*

%changelog
* Wed Feb 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.77-4]
- standarized {un}registering info pages (added make-info.patch).
- added gzipping man pages,
- added Group(pl),
- removed man group from man pages.

* Sun Nov 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.77-3]
- fixed --entry text on {un}registering info page for ed in %post
  %preun.
- added Cristian Gafton <gafton@redhat.com> patch for large file
  support in glob.

* Sat Aug  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.77-1]
- added pl translation,
- added -q %setup parameter,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- replaced "mkdir -p" with "install -d" in %install,
- removed making gmake man page as symlink to man.1,
- added using %%{name} and %%{version} macro in Source,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
  [3.76.1-3]
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- udpated from 3.75 to 3.76
- various spec file cleanups
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
