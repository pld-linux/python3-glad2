Summary:	Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs
Summary(pl.UTF-8):	Wielojęzykowy generator loaderów GL/GLES/EGL/GLX/WGL oparty na oficjalnych specyfikacjach
Name:		python3-glad2
Version:	2.0.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/glad2/
Source0:	https://files.pythonhosted.org/packages/source/g/glad2/glad2-%{version}.tar.gz
# Source0-md5:	368e14783a5fb41f72999cf0c8265704
URL:		https://pypi.org/project/glad2/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
Obsoletes:	python3-glad < 1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glad uses the official Khronos-XML specs to generate a
GL/GLES/EGL/GLX/WGL Loader made for your needs.

%description -l pl.UTF-8
Glad wykorzystuje oficjalne specyfikacje Khronos-XML do generowania
loaderów GL/GLES/EGL/GLX/WGL zgodnych z potrzebami.

%prep
%setup -q -n glad2-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

ln -s glad $RPM_BUILD_ROOT%{_bindir}/glad-3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/glad
%attr(755,root,root) %{_bindir}/glad-3
%{py3_sitescriptdir}/glad
%{py3_sitescriptdir}/glad2-%{version}-py*.egg-info
