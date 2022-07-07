
Name:           Calculator
Version:        0.1
Release:        alt4

Summary:        Calculatot dictionary
License:        GPL
Group:          Others

Packager:       SoVa

BuildRequires:  gcc-c++-common

Source0:        %name-%version.tar

%description
This package contains a simple Calculator program in C++

%prep

%setup -q

%build

%cmake
%cmake_build

%install
cd %_build_alias
mkdir -p %buildroot%_bindir/
chmod 755 %name
cp %name %buildroot%_bindir/


%files
%_bindir/%name

%changelog
* Thu Jul 7 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-alt4
- Added CMakeList.txt

* Sun Jun 26 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-alt3
- Added BuildRequires

* Sun Jun 26 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-alt2
- new rel

* Mon Jun 20 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-1
- start calculator



