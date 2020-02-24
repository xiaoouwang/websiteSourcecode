+++
title = "Overview"
date = 2019-12-21
toc = true  # Show table of contents? true/false
type = "docs"  # Do not modify.
+++

## COMMON BLOGDOWN AND KNITR OPTIONS

[rstudio git bug](https://github.com/STAT545-UBC/Discussion/issues/93)
```{}
error: unable to read askpass response from 'rpostback-askpass'
# solution git push -u origin master
```

[bookdown](https://bookdown.org/yihui/blogdown/get-started.html) [knitr](https://yihui.org/knitr/options/#chunk-options) [knitr](https://yihui.org/knitr/demo/showcase/) [knitr](https://yihui.org/knitr/demos/) [rmarkdown](https://bookdown.org/yihui/rmarkdown/) [rmarkdown2GlobalOptions](https://rmarkdown.rstudio.com/lesson-3.html)

```{r,eval=FALSE}
# auteur et extension par defaut de chaque billet
options(blogdown.ext = ".Rmd", blogdown.author = "John Doe")
# r chunk options
# echo : show source code, comment : show ##, cache : faster generation, warning : warning message,
eval = FALSE, include = FALSE, cache = TRUE, dpi = 100, echo = TRUE, comment = NA,
```

## MES LIVRES PREFERES SUR R

For a list of books on R that I read and like, please see below

[A linguist's R book collection]({{< relref "1-fileManipulation.markdown" >}})

## LISTE DES ARTICLES

`cf le menu de droite pour voir le sommaire de chaque articles`

* [manipulation de fichiers dans R]({{< relref "1-fileManipulation.markdown" >}})

