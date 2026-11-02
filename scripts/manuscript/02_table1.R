# Stage 2: Table 1 -- unweighted n and weighted % by interview language, BRFSS and CHIS.
# usage: Rscript 02_table1.R
source("/home/mo2273/ace_manuscript/scripts/common.R")
b <- readRDS(file.path(DAT, "brfss_analytic.rds")); ch <- readRDS(file.path(DAT, "chis_analytic.rds"))

lab_b <- list(
  agegrp = c(`1` = "18-24", `2` = "25-34", `3` = "35-44", `4` = "45-54", `5` = "55-64", `6` = "65+", `9` = "Don't know/refused"),
  sex = c(`1` = "Male", `2` = "Female"),
  educ = c(`1` = "Never attended/kindergarten", `2` = "Grades 1-8", `3` = "Grades 9-11", `4` = "Grade 12/GED",
           `5` = "College 1-3 years", `6` = "College 4+ years", `9` = "Refused"),
  inc = c(`1` = "<$15,000", `2` = "$15,000-24,999", `3` = "$25,000-34,999", `4` = "$35,000-49,999", `5` = "$50,000+", `9` = "Missing/DK/refused"),
  year = setNames(as.character(2019:2025), 2019:2025),
  region = c(`1` = "Northeast", `2` = "Midwest", `3` = "South", `4` = "West"))
b[, agegrp := fcase(agecat == 1, 1L, agecat %in% 2:3, 2L, agecat %in% 4:5, 3L, agecat %in% 6:7, 4L, agecat %in% 8:9, 5L,
                    agecat %in% 10:13, 6L, agecat == 14, 9L)]
lab_c <- list(
  agegrp = c(`1` = "18-25", `2` = "26-34", `3` = "35-44", `4` = "45-54", `5` = "55-64", `6` = "65+"),
  sex = c(`1` = "Male", `2` = "Female"),
  educ = c(`1` = "No formal education or grades 1-8", `2` = "Grades 9-11", `3` = "Grade 12/high school diploma", `4` = "Some college",
           `5` = "Vocational school", `6` = "AA/AS degree", `7` = "BA/BS degree or some graduate school", `8` = "MA/MS degree",
           `9` = "PhD or equivalent"),
  pov = c(`1` = "0-99% FPL", `2` = "100-199% FPL", `3` = "200-299% FPL", `4` = "300%+ FPL"),
  year = setNames(as.character(2021:2025), 2021:2025),
  fb = c(`0` = "Born in US", `1` = "Born outside US"),
  pctlf = c(`1` = "0-20%", `2` = "21-40%", `3` = "41-60%", `4` = "61-80%", `5` = "81-100% (incl. all US-born)"),
  web = c(`0` = "Phone (interviewer)", `1` = "Web (self-administered)"),
  spk_eng = c(`1` = "Speaks only English", `2` = "Very well/well", `3` = "Not well/not at all"))
ch[, agegrp := fcase(agecat == 18, 1L, agecat %in% c(26, 30), 2L, agecat %in% c(35, 40), 3L, agecat %in% c(45, 50), 4L,
                     agecat %in% c(55, 60), 5L, agecat >= 65, 6L)]
vlab <- c(agegrp = "Age group", sex = "Sex", educ = "Education", inc = "Household income", pov = "Poverty level (FPL)",
          year = "Survey year", region = "Census region", fb = "Nativity", pctlf = "Percent of life in US",
          web = "Interview mode", spk_eng = "English proficiency")

tab1 <- function(d, labs, survey) {
  rbindlist(lapply(names(labs), function(v) {
    L <- labs[[v]]
    rbindlist(lapply(names(L), function(k) {
      row <- data.table(survey = survey, variable = vlab[[v]], category = L[[k]])
      for (g in c(0, 1)) {
        s <- d[sp == g]; sel <- s[[v]] == as.numeric(k)
        nm <- if (g == 1) "Spanish" else "English"
        row[, paste0(nm, "_n") := sum(sel)]
        row[, paste0(nm, "_wpct") := 100 * sum(s$w[sel]) / sum(s$w)]
      }
      row[, Total_n := sum(d[[v]] == as.numeric(k))]
      row[, Total_wpct := 100 * sum(d$w[d[[v]] == as.numeric(k)]) / sum(d$w)]
      row
    }))
  }))
}
t1b <- tab1(b, lab_b, "BRFSS 2019-2025"); t1c <- tab1(ch, lab_c, "CHIS 2021-2025")
# check every row is accounted for
for (x in list(list(b, lab_b, t1b), list(ch, lab_c, t1c))) {
  chk <- x[[3]][, .(n = sum(Total_n)), by = variable]; stopifnot(all(chk$n == nrow(x[[1]])))
}
t1 <- rbind(t1b, t1c)
fwrite(t1, file.path(AN, "table1.csv"))

md <- function(t, title, d) {
  hdr <- sprintf("**%s** (English interview n = %s; Spanish interview n = %s)\n\n| Characteristic | English n | English %% (wtd) | Spanish n | Spanish %% (wtd) |\n|---|---:|---:|---:|---:|",
                 title, format(sum(d$sp == 0), big.mark = ","), format(sum(d$sp == 1), big.mark = ","))
  rows <- character(0); cur <- ""
  for (i in seq_len(nrow(t))) {
    if (t$variable[i] != cur) { rows <- c(rows, sprintf("| *%s* | | | | |", t$variable[i])); cur <- t$variable[i] }
    rows <- c(rows, sprintf("| %s | %s | %.1f | %s | %.1f |", t$category[i], format(t$English_n[i], big.mark = ","), t$English_wpct[i],
                            format(t$Spanish_n[i], big.mark = ","), t$Spanish_wpct[i]))
  }
  paste(c(hdr, rows), collapse = "\n")
}
txt <- paste0("## Table 1. Sample characteristics by interview language (Hispanic adults)\n\n",
              md(t1b, "BRFSS 2019-2025", b), "\n\n", md(t1c, "CHIS 2021-2025", ch),
              "\n\nn = unweighted count; % = weighted column percentage (BRFSS final weight / 7; CHIS RAKEDW0 / 5). ",
              "Age groups are collapsed for display only; models use the native 5-year groups (BRFSS _AGEG5YR 1-13 plus DK/refused; CHIS SRAGE_P1 14 groups).\n")
writeLines(txt, file.path(AN, "table1.md"))
status("Stage 2 Table 1 done: analysis/table1.csv, analysis/table1.md")
cat(txt)
