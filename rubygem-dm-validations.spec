# Generated from dm-validations-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	dm-validations

Summary:	Library for performing validations on DM models and pure Ruby object
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	3
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
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/formats
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/formats/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/support/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/validators
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/validators/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-2
+ Revision: 774206
- fix files listed twice
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 767070
- imported package rubygem-dm-validations

