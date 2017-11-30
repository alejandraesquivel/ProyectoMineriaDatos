dataSet <- read.csv("DATA.csv", header = T)
hist(dataSet$Age, main = "Nivel Educación", xlab = "nivel", breaks = 6)


y <- hist(dataSet$educationLevel, breaks = c(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), xlim = c(0,20), freq = TRUE,plot=FALSE)
#jpeg("escolaridad7.jpg")
plot(y, ylim = c(0, max(y$counts)), main = "Nivel de Educación", xlab = "escolaridad", ylab = "alumnos")
text(y$mids,y$counts+3,y$counts, cex = 0.8)

x11()
y <- hist(dataSet$Age,plot=FALSE, breaks = c(24,35,45,56,67))
plot(y, main = "Rango de Edad", xlab = "edad", ylab = "personas")
text(y$mids,y$counts+3,y$counts, cex = 0.8)

summary(data$educationLevel)
summary(dataSet$Race)
summary(dataSet$Age)
