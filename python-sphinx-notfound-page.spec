%define module sphinx-notfound-page
%define uname sphinx_notfound_page

Name:		python-%{module}
Version:	1.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{uname}-%{version}.tar.gz
Summary:	Sphinx extension to build a 404 page with absolute URLs
URL:		https://pypi.org/project/sphinx-notfound-page/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-flit-core

%description
Sphinx extension to build a 404 page with absolute URLs

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%py_build

%install
%py3_install

%files
%{py_sitedir}/notfound/
%{py_sitedir}/%{uname}-%{version}*dist-info/
%doc README.rst
%license LICENSE
