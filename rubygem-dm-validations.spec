# Generated from dm-validations-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	dm-validations

Summary:	Library for performing validations on DM models and pure Ruby object
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-validations
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Library for performing validations on DM models and pure Ruby object

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/formats
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/validators
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/validators/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/formats/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-validations
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/dm-validations/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
