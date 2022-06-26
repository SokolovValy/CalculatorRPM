Summary:        Calculatot dictionary
Name:           calculator
Version:        0.1
Release:        alt2
License:        GPL
Group:          Others
Source0:        %{name}-%{version}.tar
Packager:       SoVa

%description
This package contains a simple cailculator program in C++

%prep
%setup -q

%build
ls -la
g++ -o Calctest calc.cpp

%install
mkdir -p %buildroot%_bindir/
chmod 755 Calctest
cp Calctest %buildroot%_bindir/

%files
%_bindir/Calctest

%changelog
* Sun Jun 26 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-alt2
- new rel

* Mon Jun 20 2022 SoVa <sokolovvaly.158@gmail.com> - 0.1-1
- start calculator



