%global tl_name metanorma
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.0
Release:	%{tl_revision}.1
Summary:	Write Metanorma standardization documents using LaTe
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/metanorma
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metanorma.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metanorma.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
metanorma This work includes a LaTeX document class, a `latexml` script
and a `latexmlpost` stylesheet which allow you to write a LaTeX document
and transcode it into Metanorma's `ADOC` format. This work is sponsored
by Ribose Inc. (<https://www.ribose.com>). This work is maintained by
Ribose Inc. (<open.source@ribose.com>).

