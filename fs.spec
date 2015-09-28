#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fs
Version  : 0.5.3
Release  : 7
URL      : https://pypi.python.org/packages/source/f/fs/fs-0.5.3.tar.gz
Source0  : https://pypi.python.org/packages/source/f/fs/fs-0.5.3.tar.gz
Summary  : Filesystem abstraction layer
Group    : Development/Tools
License  : BSD-3-Clause
Requires: fs-bin
Requires: fs-python
BuildRequires : ecdsa-python
BuildRequires : fuse-dev
BuildRequires : nose
BuildRequires : paramiko-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycrypto
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
PyFilesystem
============
PyFilesystem is an abstraction layer for *filesystems*. In the same way that Python's file-like objects provide a common way of accessing files, PyFilesystem provides a common way of accessing entire filesystems. You can write platform-independent code to work with local files, that also works with any of the supported filesystems (zip, ftp, S3 etc.).

%package bin
Summary: bin components for the fs package.
Group: Binaries

%description bin
bin components for the fs package.


%package python
Summary: python components for the fs package.
Group: Default

%description python
python components for the fs package.


%prep
%setup -q -n fs-0.5.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python /usr/bin/nosetests fs.tests -v || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fscat
/usr/bin/fscp
/usr/bin/fsinfo
/usr/bin/fsls
/usr/bin/fsmkdir
/usr/bin/fsmount
/usr/bin/fsmv
/usr/bin/fsrm
/usr/bin/fsserve
/usr/bin/fstree

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
