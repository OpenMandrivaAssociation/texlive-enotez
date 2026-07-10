%global tl_name enotez
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.10d
Release:	%{tl_revision}.1
Summary:	Support for end-notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/enotez
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows nested endnotes, supports hyperref and provides means
for easy customization of the list of notes. The package requires the
expl3 bundle and packages from the LaTeX 3 'package set'.

