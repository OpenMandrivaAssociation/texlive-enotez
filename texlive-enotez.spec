Name:		texlive-enotez
Version:	61490
Release:	2
Summary:	Support for end-notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/enotez
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows nested endnotes, supports hyperref and
provides means for easy customization of the list of notes. The
package requires the expl3 bundle and packages from the LaTeX 3
'package set'.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/enotez
%doc %{_texmfdistdir}/doc/latex/enotez

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
