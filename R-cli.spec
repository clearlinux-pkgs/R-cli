#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cli
Version  : 2.0.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/cli_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cli_2.0.1.tar.gz
Summary  : Helpers for Developing Command Line Interfaces
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
Requires: R-crayon
Requires: R-fansi
Requires: R-glue
BuildRequires : R-assertthat
BuildRequires : R-crayon
BuildRequires : R-fansi
BuildRequires : R-glue
BuildRequires : buildreq-R

%description
cli
===
> Helpers for Developing Command Line Interfaces
[![Linux Build
Status](https://api.travis-ci.org/r-lib/cli.svg?branch=master)](https://travis-ci.org/r-lib/cli)
[![Windows Build
status](https://ci.appveyor.com/api/projects/status/github/r-lib/cli?svg=true)](https://ci.appveyor.com/project/gaborcsardi/cli)
[![](http://www.r-pkg.org/badges/version/cli)](http://www.r-pkg.org/pkg/cli)
[![CRAN RStudio mirror
downloads](http://cranlogs.r-pkg.org/badges/cli)](http://www.r-pkg.org/pkg/cli)
[![Coverage
Status](https://img.shields.io/codecov/c/github/r-lib/cli/master.svg)](https://codecov.io/github/r-lib/cli?branch=master)

%prep
%setup -q -c -n cli

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578527158

%install
export SOURCE_DATE_EPOCH=1578527158
rm -rf %{buildroot}
export LANG=C.UTF-8
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cli || :


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
/usr/lib64/R/library/cli/Meta/vignette.rds
/usr/lib64/R/library/cli/NAMESPACE
/usr/lib64/R/library/cli/NEWS.md
/usr/lib64/R/library/cli/R/cli
/usr/lib64/R/library/cli/R/cli.rdb
/usr/lib64/R/library/cli/R/cli.rdx
/usr/lib64/R/library/cli/R/sysdata.rdb
/usr/lib64/R/library/cli/R/sysdata.rdx
/usr/lib64/R/library/cli/doc/index.html
/usr/lib64/R/library/cli/doc/pluralization.R
/usr/lib64/R/library/cli/doc/pluralization.Rmd
/usr/lib64/R/library/cli/doc/pluralization.html
/usr/lib64/R/library/cli/examples/apps/news.R
/usr/lib64/R/library/cli/examples/apps/outdated.R
/usr/lib64/R/library/cli/examples/apps/search.R
/usr/lib64/R/library/cli/examples/apps/up.R
/usr/lib64/R/library/cli/help/AnIndex
/usr/lib64/R/library/cli/help/aliases.rds
/usr/lib64/R/library/cli/help/cli.rdb
/usr/lib64/R/library/cli/help/cli.rdx
/usr/lib64/R/library/cli/help/paths.rds
/usr/lib64/R/library/cli/html/00Index.html
/usr/lib64/R/library/cli/html/R.css
/usr/lib64/R/library/cli/logo.txt
/usr/lib64/R/library/cli/scripts/news.R
/usr/lib64/R/library/cli/scripts/outdated.R
/usr/lib64/R/library/cli/scripts/search.R
/usr/lib64/R/library/cli/scripts/up.R
/usr/lib64/R/library/cli/tests/testthat.R
/usr/lib64/R/library/cli/tests/testthat/helper-app.R
/usr/lib64/R/library/cli/tests/testthat/helper.R
/usr/lib64/R/library/cli/tests/testthat/test-alerts.R
/usr/lib64/R/library/cli/tests/testthat/test-assertions.R
/usr/lib64/R/library/cli/tests/testthat/test-box-styles.R
/usr/lib64/R/library/cli/tests/testthat/test-boxes.R
/usr/lib64/R/library/cli/tests/testthat/test-cat-helpers.R
/usr/lib64/R/library/cli/tests/testthat/test-cat.R
/usr/lib64/R/library/cli/tests/testthat/test-cliapp-output.R
/usr/lib64/R/library/cli/tests/testthat/test-collapsing.R
/usr/lib64/R/library/cli/tests/testthat/test-containers.R
/usr/lib64/R/library/cli/tests/testthat/test-crayon-combine.R
/usr/lib64/R/library/cli/tests/testthat/test-crayon-make.R
/usr/lib64/R/library/cli/tests/testthat/test-crayon.R
/usr/lib64/R/library/cli/tests/testthat/test-css.R
/usr/lib64/R/library/cli/tests/testthat/test-custom-handler.R
/usr/lib64/R/library/cli/tests/testthat/test-headers.R
/usr/lib64/R/library/cli/tests/testthat/test-inline.R
/usr/lib64/R/library/cli/tests/testthat/test-lists.R
/usr/lib64/R/library/cli/tests/testthat/test-non-breaking-space.R
/usr/lib64/R/library/cli/tests/testthat/test-pluralization.R
/usr/lib64/R/library/cli/tests/testthat/test-rules.R
/usr/lib64/R/library/cli/tests/testthat/test-sitrep.R
/usr/lib64/R/library/cli/tests/testthat/test-spinners.R
/usr/lib64/R/library/cli/tests/testthat/test-status-bar.R
/usr/lib64/R/library/cli/tests/testthat/test-subprocess.R
/usr/lib64/R/library/cli/tests/testthat/test-substitution.R
/usr/lib64/R/library/cli/tests/testthat/test-text.R
/usr/lib64/R/library/cli/tests/testthat/test-themes.R
/usr/lib64/R/library/cli/tests/testthat/test-tree.R
/usr/lib64/R/library/cli/tests/testthat/test-utils.R
/usr/lib64/R/library/cli/tests/testthat/test.R
