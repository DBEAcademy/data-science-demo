library(vcd)
install.packages("mosaic")
data("Titanic")
attach(Titanic)
mosaic(Titanic, gp = shading_hcl, gp_args = list(interpolate = c(1, 1.8)))
