Name:           npgsql
Version:        2.2.7
Release:        0.xamarin.1
License:        npgsql
Url:            http://www.npgsql.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  mono-devel
BuildArch:	    noarch
Source0:        %{name}_%{version}+dfsg3.orig.tar.gz
Source1:	npgsql.pc
Group:          System/Libraries
Summary:        PostgreSQL connector for .NET

%description
NPGSQL is an ADO.NET driver for PostgreSQL.

%prep
%setup

%build
xbuild Npgsql/Npgsql.csproj /property:Configuration=Release-net45

%install
gacutil -i Npgsql/bin/Release-net45/Npgsql.dll -package npgsql -root ${RPM_BUILD_ROOT}%{_prefix}/lib

%clean
xbuild Npgsql/Npgsql.csproj /property:Configuration=Release-net45 /target:clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README.md
%dir %{_prefix}/lib/mono/gac/Npgsql/
%{_prefix}/lib/mono/gac/Npgsql/*__*
%dir %{_prefix}/lib/mono/npgsql
%{_prefix}/lib/mono/npgsql/Npgsql.dll

%files devel
%defattr(-,root,root)
%source1

%changelog
