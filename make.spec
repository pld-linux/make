Summary:	GNU Make
Summary(de.UTF-8):	GNU Make
Summary(es.UTF-8):	GNU Make
Summary(fr.UTF-8):	L'utilitaire make de GNU
Summary(pl.UTF-8):	Narzędzie GNU Make
Summary(pt_BR.UTF-8):	GNU Make
Summary(ru.UTF-8):	GNU Make
Summary(tr.UTF-8):	GNU Make
Summary(uk.UTF-8):	GNU Make
Name:		make
Version:	3.81
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Building
Source0:	http://ftp.gnu.org/gnu/make/%{name}-%{version}.tar.gz
# Source0-md5:	a4e9494ac6dc3f6b0c5ff75c5d52abba
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ab6da7a1ba3bcf9e86e4e3fdecca61a7
Patch0:		%{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
Patch2:		%{name}-rlimit.patch
Patch3:		%{name}-jobserver.patch
Patch4:		%{name}-fdleak.patch
URL:		http://www.gnu.org/software/make/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%description -l de.UTF-8
Das MAKE-Programm dient zur Koordination der Kompilierung und zum
Linken eines Satzes von Quellen in ein Programm, wobei nur die
erforderlichen Komponenten neu kompiliert werden, so daß der
Entwickler eine Menge Zeit spart. Aber damit sind die Fähigkeiten von
MAKE noch lange nicht erschöpft - lesen Sie die Info-Dokumente.

%description -l es.UTF-8
El programa make se usa para coordinar la compilación y linkedición de
un conjunto de programas fuentes en programas ejecutables,
recompilando solamente lo que es necesario, de este modo ahorra mucho
tiempo del programador. De hecho, make puede hacer mucho más - lee la
documentación.

%description -l fr.UTF-8
make sert à coordonner la compilation et l'édition de liens d'un
ensemble de sources pour produire un programme, ne recompilant que ce
qui est nécessaire et économisant ainsi beaucoup de temps. En fait,
make peut faire beaucoup plus -- voir les docs info.

%description -l pl.UTF-8
Make jest używany do automatyzacji procesów kompilowania kodu
źródłowego i konsolidacji kodu programów wykonując tylko te czynności
które są potrzebne w razie modyfikacji plików przetwarzanych przez
make oszczędzając tym samym czas. Make może wykonywać o wiele więcej
różnych typów operacji związanych z przedtwarzaniem wsadowym. Pełen
opis make znaleźć można na stronach info ("info make").

%description -l pt_BR.UTF-8
O programa make é usado para coordenar a compilação e linkedição de um
conjunto de programas fontes em programas executáveis, recompilando
somente o que é necessário, desse modo economizando um grande tempo do
programador. De fato, make pode fazer muito mais - leia a
documentação.

%description -l ru.UTF-8
Программа make используется для управления процессом компилляции и
линковки набора исходных текстов в программу, перекомпилляции только
того, что необходимо и сохранения, таким образом, кучи времени
разработчику. На самом деле, она может намного больше - прочитайте
документацию в формате info...

%description -l tr.UTF-8
Bu program kaynak kodlarının derlenmesini ve bağlanmasını koordine
etmek için kullanılır. Sadece gerekli olan programları tekrar
derleyerek zaman yitirilmesini önler.

%description -l uk.UTF-8
Програма make використовується для керування процесом компіляції та
лінковки набору вихідних текстів у програму, перекомпіляції тільки
того, що потрібно і збереженні, таким чином, часу програміста.
Фактично, make може набагато більше - прочитайте документацію в
форматі info...

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/env.d,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf make $RPM_BUILD_ROOT%{_bindir}/gmake

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

echo '#MAKE="%{_bindir}/make -j2"' > $RPM_BUILD_ROOT/etc/env.d/MAKE

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%env_update

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
%env_update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/MAKE
%{_mandir}/man1/*
%lang(da) %{_mandir}/da/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/make.info*
