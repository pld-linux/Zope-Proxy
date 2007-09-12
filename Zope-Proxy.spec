Summary:	Mostly-transparent wrappers around another object
Name:		Zope-Proxy
Version:	3.4.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.proxy-%{version}.tar.gz
# Source0-md5:	a9e234e90bc4a16bb62b967d4a0412c6
URL:		http://www.zope.org/
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
Requires:	Zope-Interface
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the wrapped
object only when necessary to apply the policy (e.g., access checking,
location brokering, etc.) for which the proxy is responsible.

%prep
%setup -q -n zope.proxy-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/proxy
%{py_sitedir}/zope*egg*
%{py_sitedir}/zope*pth
