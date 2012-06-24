Summary:     GNU Make
Summary(de): GNU Make
Summary(fr): L'utilitaire make de GNU
Summary(pl): GNU Make
Summary(tr): GNU Make
Name:        make
Version:     3.77
Release:     3
Copyright:   GPL
Group:       Development/Building
Source:      ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

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

%build
./configure --prefix=/usr
make "CFLAGS=$RPM_OPT_FLAGS" 

%install
rm -f $RPM_BUILD_ROOT/usr/info/make.info*
install -d $RPM_BUILD_ROOT/usr/man/man1

make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/make.info*
strip $RPM_BUILD_ROOT/usr/bin/make

%post
/sbin/install-info /usr/info/make.info.gz /usr/info/dir --entry \
"* GNU make: (make).                             The GNU make utility."

%preun
/sbin/install-info --delete /usr/info/make.info.gz /usr/info/dir --entry \
"* GNU make: (make).                             The GNU make utility."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS README
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*
/usr/info/make.info*

%changelog
* Sun Nov 22 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.77-3]
- fixed --entry text on {un}registering info page for ed in %post
  %preun.
- added Cristian Gafton <gafton@redhat.com> patch for large file
  support in glob.

* Sat Aug  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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
