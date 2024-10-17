Name:		texlive-gchords
Version:	29803
Release:	2
Summary:	Typeset guitar chords
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/gchords
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
