#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Rickshaw
Version  : 1.5.0.0
Release  : 14
URL      : https://pypi.python.org/packages/source/X/XStatic-Rickshaw/XStatic-Rickshaw-1.5.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Rickshaw/XStatic-Rickshaw-1.5.0.0.tar.gz
Summary  : Rickshaw 1.5.0 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Rickshaw-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Rickshaw
--------------
Rickshaw JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Rickshaw package.
Group: Default

%description python
python components for the XStatic-Rickshaw package.


%prep
%setup -q -n XStatic-Rickshaw-1.5.0.0

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
