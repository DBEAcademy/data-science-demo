install.packages("sqldf")
library(sqldf)

query = "select * from file WHERE land =='Deutschland'"
subset <- read.csv.sql ("https://raw.githubusercontent.com/DBEAcademy/data-science-demo/main/beispiel_daten.csv", sql = query)
View(subset)
