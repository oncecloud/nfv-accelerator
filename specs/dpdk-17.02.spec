# Copyright (2016, ) Institute of Software, Chinese Academy of Sciences
# Author wuheng@otcaix.iscas.ac.cn
# Date   2016-11-18
# Copyright (2016, ) Institute of Software, Chinese Academy of Sciences
# Author wuheng@otcaix.iscas.ac.cn
# Date   2016-11-18

Name: dpdk
Version: 17.02
Release: ostack%{?dist}
Source:  dpdk-17.02.tar.gz
Summary: Automates deployment of containerized applications
License: ASL 2.0

%description
dpdk

%prep
%setup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/cba
cp -r /root/rpmbuild/BUILD/%{name}-%{version} %{buildroot}/cba

%files
/cba
