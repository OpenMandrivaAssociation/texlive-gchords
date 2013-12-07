# revision 29803
# category Package
# catalog-ctan /graphics/gchords
# catalog-date 2012-06-04 13:21:54 +0200
# catalog-license gpl
# catalog-version 1.20
Name:		texlive-gchords
Version:	1.20
Release:	6
Summary:	Typeset guitar chords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/gchords
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for typesetting of guitar chord diagrams,
including options for chord names, finger numbers and
typesetting above lyrics. The bundle also includes a TCL script
(chordbox.tcl) that provides a graphical application which
creates LaTeX files that use gchords.sty.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gchords/gchords.sty
%doc %{_texmfdistdir}/doc/latex/gchords/README
%doc %{_texmfdistdir}/doc/latex/gchords/chordbox.tcl
%doc %{_texmfdistdir}/doc/latex/gchords/gchords_doc.pdf
%doc %{_texmfdistdir}/doc/latex/gchords/gchords_doc.tex
%doc %{_texmfdistdir}/doc/latex/gchords/get2knowu.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
