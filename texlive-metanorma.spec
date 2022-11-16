Name:		texlive-metanorma
Version:	55010
Release:	1
Summary:	Write Metanorma standardization documents using LaTe
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metanorma
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metanorma.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metanorma.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
metanorma This work includes a LaTeX document class, a
`latexml` script and a `latexmlpost` stylesheet which allow you
to write a LaTeX document and transcode it into Metanorma's
`ADOC` format. This work is sponsored by Ribose Inc.
(<https://www.ribose.com>). This work is maintained by Ribose
Inc. (<open.source@ribose.com>).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/metanorma
%doc %{_texmfdistdir}/doc/latex/metanorma

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
