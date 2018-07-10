#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fs
Version  : 2.0.24
Release  : 39
URL      : https://github.com/PyFilesystem/pyfilesystem2/archive/v2.0.24.tar.gz
Source0  : https://github.com/PyFilesystem/pyfilesystem2/archive/v2.0.24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: fs-python3
Requires: fs-license
Requires: fs-python
Requires: appdirs
Requires: enum34
Requires: pytz
Requires: setuptools
Requires: six
Requires: typing
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-python

%description
PyFilesystem2
=============
Python's Filesystem abstraction layer.
[![PyPI version](https://badge.fury.io/py/fs.svg)](https://badge.fury.io/py/fs)
[![PyPI](https://img.shields.io/pypi/pyversions/fs.svg)](https://pypi.org/project/fs/)
[![Build Status](https://travis-ci.org/PyFilesystem/pyfilesystem2.svg?branch=master)](https://travis-ci.org/PyFilesystem/pyfilesystem2)
[![Coverage Status](https://coveralls.io/repos/github/PyFilesystem/pyfilesystem2/badge.svg)](https://coveralls.io/github/PyFilesystem/pyfilesystem2)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/30ad6445427349218425d93886ade9ee)](https://www.codacy.com/app/will-mcgugan/pyfilesystem2?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PyFilesystem/pyfilesystem2&amp;utm_campaign=Badge_Grade)
[![Code Health](https://landscape.io/github/PyFilesystem/pyfilesystem2/master/landscape.svg?style=flat)](https://landscape.io/github/PyFilesystem/pyfilesystem2/master)

%package license
Summary: license components for the fs package.
Group: Default

%description license
license components for the fs package.


%package python
Summary: python components for the fs package.
Group: Default
Requires: fs-python3

%description python
python components for the fs package.


%package python3
Summary: python3 components for the fs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the fs package.


%prep
%setup -q -n pyfilesystem2-2.0.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530989921
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/fs
cp LICENSE %{buildroot}/usr/share/doc/fs/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/fs/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
