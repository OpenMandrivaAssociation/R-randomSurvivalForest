%global packname  randomSurvivalForest
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.6.4
Release:          2
Summary:          Random Survival Forests
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/randomSurvivalForest_3.6.4.tar.gz
Requires:         R-XML 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-XML 

%description
Random survival forests for right-censored and competing risks survival

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
# %doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.6.3-1
+ Revision: 777813
- Import R-randomSurvivalForest
- Import R-randomSurvivalForest


