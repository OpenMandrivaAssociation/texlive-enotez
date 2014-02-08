# revision 27179
# category Package
# catalog-ctan /macros/latex/contrib/enotez
# catalog-date 2012-07-24 16:08:54 +0200
# catalog-license lppl1.3
# catalog-version 0.3a
Name:		texlive-enotez
Version:	0.3a
Release:	2
Summary:	Support for end-notes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/enotez
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/enotez.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows nested endnotes, supports hyperref and
provides means for easy customization of the list of notes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/enotez/enotez.sty
%doc %{_texmfdistdir}/doc/latex/enotez/README
%doc %{_texmfdistdir}/doc/latex/enotez/enotez_en.pdf
%doc %{_texmfdistdir}/doc/latex/enotez/enotez_en.tex
%doc %{_texmfdistdir}/doc/latex/enotez/enotez_split_example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3a-1
+ Revision: 813485
- Import texlive-enotez
- Import texlive-enotez

