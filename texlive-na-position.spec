Name:		texlive-na-position
Version:	55559
Release:	2
Summary:	Tables of relative positions of curves and asymptotes or tangents in Arabic documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/na-position
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/na-position.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/na-position.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package facilitates, in most cases, the creation of tables
of relative positions of a curve and its asymptote, or a curve
and a tangent in one of its points. It depends on tkz-tab and
listofitems, as well as amsmath, amsfonts, mathrsfs, and
amssymb. This package has to be used with polyglossia and
XeLaTeX to produce documents in Arabic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/na-position
%doc %{_texmfdistdir}/doc/xelatex/na-position

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
