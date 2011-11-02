Name:		texlive-gchords
Version:	1.20
Release:	1
Summary:	Typeset guitar chords
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/gchords
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX package for typesetting of guitar chord diagrams,
including options for chord names, finger numbers and
typesetting above lyrics. The bundle also includes a TCL script
(chordbox.tcl) that provides a graphical application which
creates LaTeX files that use gchords.sty.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
