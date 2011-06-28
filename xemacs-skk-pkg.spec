Summary:	Japanese Language Input Method
Summary(pl.UTF-8):	Metoda wprowadzania znaków japońskich
Name:		xemacs-skk-pkg
%define		srcname	skk
Version:	1.24
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	8735a78a15e7a9d00ec59784a16418ab
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-viper-pkg
Requires:	xemacs-mule-base-pkg
Requires:	xemacs-elib-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japanese Language Input Method.

%description -l pl.UTF-8
Metoda wprowadzania znaków japońskich.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc lisp/skk/ChangeLog
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*.info*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
