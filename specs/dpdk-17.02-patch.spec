# Copyright (2016, ) Institute of Software, Chinese Academy of Sciences
# Author wuheng@otcaix.iscas.ac.cn
# Date   2016-11-18
# Copyright (2016, ) Institute of Software, Chinese Academy of Sciences
# Author wuheng@otcaix.iscas.ac.cn
# Date   2016-11-18

Name: dpdk-patch
Version: 17.02
Release: ostack%{?dist}
Source:  dpdk-patch-17.02.tar.gz
Summary: Automates deployment of containerized applications
License: ASL 2.0

%description
dpdk

%prep
%setup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/cba/%{name}-%{version}
mkdir -p %{buildroot}/usr/bin
cp -r /root/rpmbuild/BUILD/%{name}-%{version}/*ko %{buildroot}/cba/%{name}-%{version}
cp -r /root/rpmbuild/BUILD/%{name}-%{version}/dpdk* %{buildroot}/usr/bin

%files
/cba/%{name}-%{version}
/usr/bin
