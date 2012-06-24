Summary:	GNU Make
Summary(de):	GNU Make
Summary(es):	GNU Make
Summary(fr):	L'utilitaire make de GNU
Summary(pl):	GNU Make
Summary(pt_BR):	GNU Make
Summary(ru):	GNU Make
Summary(tr):	GNU Make
Summary(uk):	GNU Make
Name:		make
Version:	3.79.1
Release:	14
Epoch:		1
License:	GPL
Group:		Development/Building
Source0:	ftp://prep.ai.mit.edu/pub/gnu/make/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-noclock_gettime.patch
Patch2:		%{name}-pl.po.patch
Patch3:		%{name}-ac250.patch
Patch4:		%{name}-expand-tilde.patch
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

%description -l de
Das MAKE-Programm dient zur Koordination der Kompilierung und zum
Linken eines Satzes von Quellen in ein Programm, wobei nur die
erforderlichen Komponenten neu kompiliert werden, so da� der
Entwickler eine Menge Zeit spart. Aber damit sind die F�higkeiten von
MAKE noch lange nicht ersch�pft - lesen Sie die Info-Dokumente.

%description -l es
El programa make se usa para coordinar la compilaci�n y linkedici�n de
un conjunto de programas fuentes en programas ejecutables,
recompilando solamente lo que es necesario, de este modo ahorra mucho
tiempo del programador. De hecho, make puede hacer mucho m�s - lee la
documentaci�n.

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

%description -l pt_BR
O programa make � usado para coordenar a compila��o e linkedi��o de um
conjunto de programas fontes em programas execut�veis, recompilando
somente o que � necess�rio, desse modo economizando um grande tempo do
programador. De fato, make pode fazer muito mais - leia a
documenta��o.

%description -l ru
��������� make ������������ ��� ���������� ��������� ����������� �
�������� ������ �������� ������� � ���������, ��������������� ������
����, ��� ���������� � ����������, ����� �������, ���� �������
������������. �� ����� ����, ��� ����� ������� ������ - ����������
������������ � ������� info...

%description -l tr
Bu program kaynak kodlar�n�n derlenmesini ve ba�lanmas�n� koordine
etmek i�in kullan�l�r. Sadece gerekli olan programlar� tekrar
derleyerek zaman yitirilmesini �nler.

%description -l uk
�������� make ����������դ���� ��� ��������� �������� ���Ц��æ� ��
̦������ ������ ��Ȧ���� ����Ԧ� � ��������, �������Ц��æ� Ԧ����
����, �� ���Ҧ��� � ��������Φ, ����� �����, ���� ������ͦ���.
��������, make ���� �������� ¦���� - ���������� ���������æ� �
�����Ԧ info...

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm missing
aclocal
%{__autoconf}
automake -a -c -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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
%lang(da) %{_mandir}/da/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/make.info*
