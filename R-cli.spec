#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cli
Version  : 3.3.0
Release  : 63
URL      : https://cran.r-project.org/src/contrib/cli_3.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cli_3.3.0.tar.gz
Summary  : Helpers for Developing Command Line Interfaces
Group    : Development/Tools
License  : MIT
Requires: R-cli-lib = %{version}-%{release}
Requires: R-glue
BuildRequires : R-glue
BuildRequires : buildreq-R

%description
# cli
> Helpers for Developing Command Line Interfaces
<!-- badges: start -->
[![R-CMD-check](https://github.com/r-lib/cli/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/r-lib/cli/actions/workflows/R-CMD-check.yaml)
[![](https://www.r-pkg.org/badges/version/cli)](https://www.r-pkg.org/pkg/cli)
[![CRAN RStudio mirror
downloads](https://cranlogs.r-pkg.org/badges/cli)](https://www.r-pkg.org/pkg/cli)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/cli/branch/main/graph/badge.svg)](https://app.codecov.io/gh/r-lib/cli?branch=main)
<!-- badges: end -->

%package lib
Summary: lib components for the R-cli package.
Group: Libraries

%description lib
lib components for the R-cli package.


%prep
%setup -q -c -n cli
cd %{_builddir}/cli

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650900241

%install
export SOURCE_DATE_EPOCH=1650900241
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cli
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
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
/usr/lib64/R/library/cli/NAMESPACE
/usr/lib64/R/library/cli/NEWS.md
/usr/lib64/R/library/cli/R/cli
/usr/lib64/R/library/cli/R/cli.rdb
/usr/lib64/R/library/cli/R/cli.rdx
/usr/lib64/R/library/cli/R/sysdata.rdb
/usr/lib64/R/library/cli/R/sysdata.rdx
/usr/lib64/R/library/cli/examples/apps/news.R
/usr/lib64/R/library/cli/examples/apps/outdated.R
/usr/lib64/R/library/cli/examples/apps/search.R
/usr/lib64/R/library/cli/examples/apps/up.R
/usr/lib64/R/library/cli/help/AnIndex
/usr/lib64/R/library/cli/help/aliases.rds
/usr/lib64/R/library/cli/help/cli.rdb
/usr/lib64/R/library/cli/help/cli.rdx
/usr/lib64/R/library/cli/help/figures/alert-danger.svg
/usr/lib64/R/library/cli/help/figures/alert-info.svg
/usr/lib64/R/library/cli/help/figures/alert-success.svg
/usr/lib64/R/library/cli/help/figures/alert-warning.svg
/usr/lib64/R/library/cli/help/figures/alert-wrap.svg
/usr/lib64/R/library/cli/help/figures/ansi-align-center.svg
/usr/lib64/R/library/cli/help/figures/ansi-align-right.svg
/usr/lib64/R/library/cli/help/figures/ansi-align.svg
/usr/lib64/R/library/cli/help/figures/ansi-column.svg
/usr/lib64/R/library/cli/help/figures/box-bg-color.svg
/usr/lib64/R/library/cli/help/figures/box-border-color.svg
/usr/lib64/R/library/cli/help/figures/box-border.svg
/usr/lib64/R/library/cli/help/figures/box-custom.svg
/usr/lib64/R/library/cli/help/figures/box-default.svg
/usr/lib64/R/library/cli/help/figures/box-float.svg
/usr/lib64/R/library/cli/help/figures/box-label-align.svg
/usr/lib64/R/library/cli/help/figures/box-lines.svg
/usr/lib64/R/library/cli/help/figures/box-padding.svg
/usr/lib64/R/library/cli/help/figures/box-text-color.svg
/usr/lib64/R/library/cli/help/figures/builtin-theme.svg
/usr/lib64/R/library/cli/help/figures/cli-abort-2.svg
/usr/lib64/R/library/cli/help/figures/cli-abort.svg
/usr/lib64/R/library/cli/help/figures/cli-blockquote.svg
/usr/lib64/R/library/cli/help/figures/cli-bullets.svg
/usr/lib64/R/library/cli/help/figures/cli-cli.svg
/usr/lib64/R/library/cli/help/figures/cli-code.svg
/usr/lib64/R/library/cli/help/figures/cli-div-close.svg
/usr/lib64/R/library/cli/help/figures/cli-div.svg
/usr/lib64/R/library/cli/help/figures/cli-dl-2.svg
/usr/lib64/R/library/cli/help/figures/cli-dl.svg
/usr/lib64/R/library/cli/help/figures/cli-end-debug.svg
/usr/lib64/R/library/cli/help/figures/cli-end-many.svg
/usr/lib64/R/library/cli/help/figures/cli-end-noid.svg
/usr/lib64/R/library/cli/help/figures/cli-end.svg
/usr/lib64/R/library/cli/help/figures/cli-format-class.svg
/usr/lib64/R/library/cli/help/figures/cli-format-default.svg
/usr/lib64/R/library/cli/help/figures/cli-format-num.svg
/usr/lib64/R/library/cli/help/figures/cli-format-theme.svg
/usr/lib64/R/library/cli/help/figures/cli-h1.svg
/usr/lib64/R/library/cli/help/figures/cli-li.svg
/usr/lib64/R/library/cli/help/figures/cli-ol-2.svg
/usr/lib64/R/library/cli/help/figures/cli-ol-3.svg
/usr/lib64/R/library/cli/help/figures/cli-ol.svg
/usr/lib64/R/library/cli/help/figures/cli-par.svg
/usr/lib64/R/library/cli/help/figures/cli-rule-line-type.svg
/usr/lib64/R/library/cli/help/figures/cli-rule.svg
/usr/lib64/R/library/cli/help/figures/cli-text-concat.svg
/usr/lib64/R/library/cli/help/figures/cli-text-containers.svg
/usr/lib64/R/library/cli/help/figures/cli-text-glue-style.svg
/usr/lib64/R/library/cli/help/figures/cli-text-glue.svg
/usr/lib64/R/library/cli/help/figures/cli-text-markup.svg
/usr/lib64/R/library/cli/help/figures/cli-text-newline.svg
/usr/lib64/R/library/cli/help/figures/cli-text.svg
/usr/lib64/R/library/cli/help/figures/cli-ul-2.svg
/usr/lib64/R/library/cli/help/figures/cli-ul.svg
/usr/lib64/R/library/cli/help/figures/cli-vec-2.svg
/usr/lib64/R/library/cli/help/figures/cli-vec.svg
/usr/lib64/R/library/cli/help/figures/cli-verbatim-2.svg
/usr/lib64/R/library/cli/help/figures/cli-verbatim.svg
/usr/lib64/R/library/cli/help/figures/cnt-auto-close.svg
/usr/lib64/R/library/cli/help/figures/cnt-debug.svg
/usr/lib64/R/library/cli/help/figures/cnt-theme.svg
/usr/lib64/R/library/cli/help/figures/demo-spinners.svg
/usr/lib64/R/library/cli/help/figures/format-error-2.svg
/usr/lib64/R/library/cli/help/figures/format-error.svg
/usr/lib64/R/library/cli/help/figures/get-spinner.svg
/usr/lib64/R/library/cli/help/figures/inline-collapse-2.svg
/usr/lib64/R/library/cli/help/figures/inline-collapse-trunc.svg
/usr/lib64/R/library/cli/help/figures/inline-collapse.svg
/usr/lib64/R/library/cli/help/figures/inline-escape-2.svg
/usr/lib64/R/library/cli/help/figures/inline-escape.svg
/usr/lib64/R/library/cli/help/figures/inline-examples.svg
/usr/lib64/R/library/cli/help/figures/inline-newclass.svg
/usr/lib64/R/library/cli/help/figures/inline-plural.svg
/usr/lib64/R/library/cli/help/figures/inline-text-2.svg
/usr/lib64/R/library/cli/help/figures/inline-text-3.svg
/usr/lib64/R/library/cli/help/figures/inline-text.svg
/usr/lib64/R/library/cli/help/figures/make-spinner-custom.svg
/usr/lib64/R/library/cli/help/figures/make-spinner-default.svg
/usr/lib64/R/library/cli/help/figures/make-spinner-template.svg
/usr/lib64/R/library/cli/help/figures/progress-1.svg
/usr/lib64/R/library/cli/help/figures/progress-after.svg
/usr/lib64/R/library/cli/help/figures/progress-along-1.svg
/usr/lib64/R/library/cli/help/figures/progress-along-2.svg
/usr/lib64/R/library/cli/help/figures/progress-along-3.svg
/usr/lib64/R/library/cli/help/figures/progress-clear.svg
/usr/lib64/R/library/cli/help/figures/progress-current.svg
/usr/lib64/R/library/cli/help/figures/progress-format.svg
/usr/lib64/R/library/cli/help/figures/progress-message.svg
/usr/lib64/R/library/cli/help/figures/progress-natotal.svg
/usr/lib64/R/library/cli/help/figures/progress-output.svg
/usr/lib64/R/library/cli/help/figures/progress-output2.svg
/usr/lib64/R/library/cli/help/figures/progress-step-dynamic.svg
/usr/lib64/R/library/cli/help/figures/progress-step-msg.svg
/usr/lib64/R/library/cli/help/figures/progress-step-spin.svg
/usr/lib64/R/library/cli/help/figures/progress-step.svg
/usr/lib64/R/library/cli/help/figures/progress-style.svg
/usr/lib64/R/library/cli/help/figures/progress-tasks.svg
/usr/lib64/R/library/cli/help/figures/progress-var-bar.svg
/usr/lib64/R/library/cli/help/figures/progress-var-current-bytes.svg
/usr/lib64/R/library/cli/help/figures/progress-var-current.svg
/usr/lib64/R/library/cli/help/figures/progress-var-elapsed-clock.svg
/usr/lib64/R/library/cli/help/figures/progress-var-elapsed-raw.svg
/usr/lib64/R/library/cli/help/figures/progress-var-elapsed.svg
/usr/lib64/R/library/cli/help/figures/progress-var-eta-raw.svg
/usr/lib64/R/library/cli/help/figures/progress-var-eta-str.svg
/usr/lib64/R/library/cli/help/figures/progress-var-eta.svg
/usr/lib64/R/library/cli/help/figures/progress-var-extra.svg
/usr/lib64/R/library/cli/help/figures/progress-var-id.svg
/usr/lib64/R/library/cli/help/figures/progress-var-name.svg
/usr/lib64/R/library/cli/help/figures/progress-var-percent.svg
/usr/lib64/R/library/cli/help/figures/progress-var-rate-bytes.svg
/usr/lib64/R/library/cli/help/figures/progress-var-rate-raw.svg
/usr/lib64/R/library/cli/help/figures/progress-var-rate.svg
/usr/lib64/R/library/cli/help/figures/progress-var-status.svg
/usr/lib64/R/library/cli/help/figures/progress-var-timestamp.svg
/usr/lib64/R/library/cli/help/figures/rule-bars.svg
/usr/lib64/R/library/cli/help/figures/rule-center-label.svg
/usr/lib64/R/library/cli/help/figures/rule-colored-label.svg
/usr/lib64/R/library/cli/help/figures/rule-colored-line.svg
/usr/lib64/R/library/cli/help/figures/rule-custom-line-2.svg
/usr/lib64/R/library/cli/help/figures/rule-custom-line-3.svg
/usr/lib64/R/library/cli/help/figures/rule-custom-line.svg
/usr/lib64/R/library/cli/help/figures/rule-double.svg
/usr/lib64/R/library/cli/help/figures/rule-left-label.svg
/usr/lib64/R/library/cli/help/figures/rule-simple.svg
/usr/lib64/R/library/cli/help/figures/simple-theme.svg
/usr/lib64/R/library/cli/help/figures/spark-bar-1.svg
/usr/lib64/R/library/cli/help/figures/spark-bar-2.svg
/usr/lib64/R/library/cli/help/figures/spark-bar-3.svg
/usr/lib64/R/library/cli/help/figures/spark-bar-na.svg
/usr/lib64/R/library/cli/help/figures/spark-line.svg
/usr/lib64/R/library/cli/help/figures/tree-colored.svg
/usr/lib64/R/library/cli/help/figures/tree-root.svg
/usr/lib64/R/library/cli/help/figures/tree-trim-mark.svg
/usr/lib64/R/library/cli/help/figures/tree-trimming.svg
/usr/lib64/R/library/cli/help/figures/tree.svg
/usr/lib64/R/library/cli/help/figures/unnamed-chunk-1.svg
/usr/lib64/R/library/cli/help/paths.rds
/usr/lib64/R/library/cli/html/00Index.html
/usr/lib64/R/library/cli/html/R.css
/usr/lib64/R/library/cli/include/cli/progress.h
/usr/lib64/R/library/cli/logo.txt
/usr/lib64/R/library/cli/scripts/news.R
/usr/lib64/R/library/cli/scripts/outdated.R
/usr/lib64/R/library/cli/scripts/search.R
/usr/lib64/R/library/cli/scripts/up.R
/usr/lib64/R/library/cli/shiny/along/app.R
/usr/lib64/R/library/cli/shiny/format/app.R
/usr/lib64/R/library/cli/shiny/nested/app.R
/usr/lib64/R/library/cli/shiny/output/app.R
/usr/lib64/R/library/cli/shiny/simple/app.R
/usr/lib64/R/library/cli/tests/testthat.R
/usr/lib64/R/library/cli/tests/testthat/_snaps/alerts.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/ansi-html.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/ansiex-2.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/ansiex.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/box-styles.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/boxes.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/bullets.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/cat-helpers.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/code.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/collapsing.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/containers.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/deep-lists.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/diff.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/format-conditions.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/glue.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/hash.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/headers.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/inline-2.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/inline.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/lists.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/meta.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/non-breaking-space.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/pluralization.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/prettycode.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-along.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-bar.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-c.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-client.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-handler-logger.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-message.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-ticking.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-types.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/progress-variables.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/rlang-errors.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/rules.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/spark.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/text.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/themes.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/tree.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/utf8/utf8-output.txt
/usr/lib64/R/library/cli/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/cli/tests/testthat/_snaps/verbatim.md
/usr/lib64/R/library/cli/tests/testthat/helper.R
/usr/lib64/R/library/cli/tests/testthat/progress-1.c
/usr/lib64/R/library/cli/tests/testthat/progress-2.c
/usr/lib64/R/library/cli/tests/testthat/progresstest/DESCRIPTION
/usr/lib64/R/library/cli/tests/testthat/progresstest/NAMESPACE
/usr/lib64/R/library/cli/tests/testthat/progresstest/R/test.R
/usr/lib64/R/library/cli/tests/testthat/progresstest/src/cleancall.c
/usr/lib64/R/library/cli/tests/testthat/progresstest/src/cleancall.h
/usr/lib64/R/library/cli/tests/testthat/progresstest/src/test.c
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/DESCRIPTION
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/NAMESPACE
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/R/cpp11.R
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/R/testcpp.R
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/src/cpp11.cpp
/usr/lib64/R/library/cli/tests/testthat/progresstestcpp/src/testcpp.cpp
/usr/lib64/R/library/cli/tests/testthat/setup.R
/usr/lib64/R/library/cli/tests/testthat/test-alerts.R
/usr/lib64/R/library/cli/tests/testthat/test-ansi-combine.R
/usr/lib64/R/library/cli/tests/testthat/test-ansi-html.R
/usr/lib64/R/library/cli/tests/testthat/test-ansi-hyperlink.R
/usr/lib64/R/library/cli/tests/testthat/test-ansi-make.R
/usr/lib64/R/library/cli/tests/testthat/test-ansi.R
/usr/lib64/R/library/cli/tests/testthat/test-ansiex-2.R
/usr/lib64/R/library/cli/tests/testthat/test-ansiex.R
/usr/lib64/R/library/cli/tests/testthat/test-assertions.R
/usr/lib64/R/library/cli/tests/testthat/test-box-styles.R
/usr/lib64/R/library/cli/tests/testthat/test-boxes.R
/usr/lib64/R/library/cli/tests/testthat/test-bullets.R
/usr/lib64/R/library/cli/tests/testthat/test-cat-helpers.R
/usr/lib64/R/library/cli/tests/testthat/test-cat.R
/usr/lib64/R/library/cli/tests/testthat/test-cliapp-output.R
/usr/lib64/R/library/cli/tests/testthat/test-code.R
/usr/lib64/R/library/cli/tests/testthat/test-collapsing.R
/usr/lib64/R/library/cli/tests/testthat/test-containers.R
/usr/lib64/R/library/cli/tests/testthat/test-css.R
/usr/lib64/R/library/cli/tests/testthat/test-custom-handler.R
/usr/lib64/R/library/cli/tests/testthat/test-deep-lists.R
/usr/lib64/R/library/cli/tests/testthat/test-diff.R
/usr/lib64/R/library/cli/tests/testthat/test-format-conditions.R
/usr/lib64/R/library/cli/tests/testthat/test-glue.R
/usr/lib64/R/library/cli/tests/testthat/test-hash.R
/usr/lib64/R/library/cli/tests/testthat/test-headers.R
/usr/lib64/R/library/cli/tests/testthat/test-inline-2.R
/usr/lib64/R/library/cli/tests/testthat/test-inline.R
/usr/lib64/R/library/cli/tests/testthat/test-lists.R
/usr/lib64/R/library/cli/tests/testthat/test-meta.R
/usr/lib64/R/library/cli/tests/testthat/test-non-breaking-space.R
/usr/lib64/R/library/cli/tests/testthat/test-num-ansi-colors.R
/usr/lib64/R/library/cli/tests/testthat/test-pluralization.R
/usr/lib64/R/library/cli/tests/testthat/test-prettycode.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-along.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-bar.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-c.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-client.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-handler-logger.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-handler-say.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-handlers.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-message.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-ticking.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-types.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-utils.R
/usr/lib64/R/library/cli/tests/testthat/test-progress-variables.R
/usr/lib64/R/library/cli/tests/testthat/test-rlang-errors.R
/usr/lib64/R/library/cli/tests/testthat/test-rules.R
/usr/lib64/R/library/cli/tests/testthat/test-sitrep.R
/usr/lib64/R/library/cli/tests/testthat/test-spark.R
/usr/lib64/R/library/cli/tests/testthat/test-spinners.R
/usr/lib64/R/library/cli/tests/testthat/test-status-bar.R
/usr/lib64/R/library/cli/tests/testthat/test-subprocess.R
/usr/lib64/R/library/cli/tests/testthat/test-substitution.R
/usr/lib64/R/library/cli/tests/testthat/test-suppress.R
/usr/lib64/R/library/cli/tests/testthat/test-text.R
/usr/lib64/R/library/cli/tests/testthat/test-themes.R
/usr/lib64/R/library/cli/tests/testthat/test-timer.R
/usr/lib64/R/library/cli/tests/testthat/test-tree.R
/usr/lib64/R/library/cli/tests/testthat/test-utf8.R
/usr/lib64/R/library/cli/tests/testthat/test-utils.R
/usr/lib64/R/library/cli/tests/testthat/test-verbatim.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/cli/libs/cli.so
/usr/lib64/R/library/cli/libs/cli.so.avx2
/usr/lib64/R/library/cli/libs/cli.so.avx512
