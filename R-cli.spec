#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cli
Version  : 1.0.0
Release  : 4
URL      : https://cran.r-project.org/src/contrib/cli_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cli_1.0.0.tar.gz
Summary  : Helpers for Developing Command Line Interfaces
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
Requires: R-mockery
Requires: R-withr
BuildRequires : R-assertthat
BuildRequires : R-mockery
BuildRequires : R-withr
BuildRequires : clr-R-helpers

%description
interfaces ('CLIs'). Includes tools for drawing rules, boxes, trees, and
    'Unicode' symbols with 'ASCII' alternatives.

%prep
%setup -q -c -n cli

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523294349

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523294349
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cli
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cli
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cli
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library cli|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cli/DESCRIPTION
/usr/lib64/R/library/cli/INDEX
/usr/lib64/R/library/cli/LICENSE
/usr/lib64/R/library/cli/Meta/Rd.rds
/usr/lib64/R/library/cli/Meta/features.rds
/usr/lib64/R/library/cli/Meta/hsearch.rds
/usr/lib64/R/library/cli/Meta/links.rds
/usr/lib64/R/library/cli/Meta/nsInfo.rds
/usr/lib64/R/library/cli/Meta/package.rds
/usr/lib64/R/library/cli/NAMESPACE
/usr/lib64/R/library/cli/NEWS.md
/usr/lib64/R/library/cli/R/cli
/usr/lib64/R/library/cli/R/cli.rdb
/usr/lib64/R/library/cli/R/cli.rdx
/usr/lib64/R/library/cli/R/sysdata.rdb
/usr/lib64/R/library/cli/R/sysdata.rdx
/usr/lib64/R/library/cli/help/AnIndex
/usr/lib64/R/library/cli/help/aliases.rds
/usr/lib64/R/library/cli/help/cli.rdb
/usr/lib64/R/library/cli/help/cli.rdx
/usr/lib64/R/library/cli/help/figures/box-1.png
/usr/lib64/R/library/cli/help/figures/box-bgcolor-1.png
/usr/lib64/R/library/cli/help/figures/box-bgcolor-2.png
/usr/lib64/R/library/cli/help/figures/box-border-color-1.png
/usr/lib64/R/library/cli/help/figures/box-border-color-2.png
/usr/lib64/R/library/cli/help/figures/box-border-style-1.png
/usr/lib64/R/library/cli/help/figures/box-color-1.png
/usr/lib64/R/library/cli/help/figures/box-customized-1.png
/usr/lib64/R/library/cli/help/figures/box-floating-1.png
/usr/lib64/R/library/cli/help/figures/box-floating-2.png
/usr/lib64/R/library/cli/help/figures/box-label-align-1.png
/usr/lib64/R/library/cli/help/figures/box-label-align-2.png
/usr/lib64/R/library/cli/help/figures/box-label-align-3.png
/usr/lib64/R/library/cli/help/figures/box-lines-1.png
/usr/lib64/R/library/cli/help/figures/box-margin-1.png
/usr/lib64/R/library/cli/help/figures/box-margin-2.png
/usr/lib64/R/library/cli/help/figures/box-margin-3.png
/usr/lib64/R/library/cli/help/figures/box-padding-1.png
/usr/lib64/R/library/cli/help/figures/box-padding-2.png
/usr/lib64/R/library/cli/help/figures/rule-1.png
/usr/lib64/R/library/cli/help/figures/rule-bars-1.png
/usr/lib64/R/library/cli/help/figures/rule-bars-2.png
/usr/lib64/R/library/cli/help/figures/rule-center-1.png
/usr/lib64/R/library/cli/help/figures/rule-color-1.png
/usr/lib64/R/library/cli/help/figures/rule-color-label-1.png
/usr/lib64/R/library/cli/help/figures/rule-color-line-1.png
/usr/lib64/R/library/cli/help/figures/rule-double-1.png
/usr/lib64/R/library/cli/help/figures/rule-left-1.png
/usr/lib64/R/library/cli/help/figures/rule-line-custom-1.png
/usr/lib64/R/library/cli/help/figures/rule-line-custom-2-1.png
/usr/lib64/R/library/cli/help/figures/rule-line-custom-3-1.png
/usr/lib64/R/library/cli/help/figures/tree-1.png
/usr/lib64/R/library/cli/help/figures/tree-color-1.png
/usr/lib64/R/library/cli/help/paths.rds
/usr/lib64/R/library/cli/html/00Index.html
/usr/lib64/R/library/cli/html/R.css
