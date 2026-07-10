%global tl_name gchords
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	Typeset guitar chords
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/gchords
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gchords.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for typesetting of guitar chord diagrams, including
options for chord names, finger numbers and typesetting above lyrics.
The bundle also includes a TCL script (chordbox.tcl) that provides a
graphical application which creates LaTeX files that use gchords.sty.

