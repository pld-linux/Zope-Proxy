Summary:	Mostly-transparent wrappers around another object
Summary(pl.UTF-8):	Prawie przezroczyste obudowywanie innych obiektów
Name:		Zope-Proxy
Version:	3.4.2
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.proxy/zope.proxy-%{version}.zip
# Source0-md5:	ad51f25d4d86be7cfebb70bd77421f92
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
%pyrequires_eq	python-modules
Requires:	Zope-Interface
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the
wrapped object only when necessary to apply the policy (e.g., access
checking, location brokering, etc.) for which the proxy is
responsible.

%description -l pl.UTF-8
Proxy to specjalne obiekty służące jako prawie przezroczyste
obudowanie innego obiektu, wkraczające w zwykłe zachowanie
obudowywanego obiektu tylko w razie potrzeby, aby zastosować politykę
(np. kontrolę dostępu, pośredniczenie itp.), za którą odpowiada proxy.

%prep
%setup -q -n zope.proxy-%{version}

%build
export CFLAGS="%{rpmcflags}"
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
rm $RPM_BUILD_ROOT%{py_sitedir}/zope/proxy/*.[ch]
rm -r $RPM_BUILD_ROOT%{py_sitedir}/zope/proxy/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/zope/proxy
%{py_sitedir}/zope/proxy/*.cfg
%{py_sitedir}/zope/proxy/*.py[co]
%attr(755,root,root) %{py_sitedir}/zope/proxy/_zope_proxy_proxy.so
%{py_sitedir}/zope.proxy-*.egg-info
%{py_sitedir}/zope.proxy-*-nspkg.pth

# -devel?
#%{py_incdir}/zope.proxy
