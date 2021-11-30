###Bar Graph Example###

graph1 <- data.frame(CloudSoftware=c("NoSQL", "Pig", "MapReduce", "Hive", "Hadoop"),
Weight=c("0.202","0.196","0.192","0.182","0.161"))

g <- ggplot(graph1, aes(x = CloudSoftware, y = Weight))+
geom_col(color="black", fill="lightblue")+
geom_text(aes(label=Weight), vjust=1.6, color="white",
position = position_dodge(0.9), size=3.5)

g + labs(title = "Cloud Software Weights by Programming Language Required", x = "Cloud Software", y = "Correlation")

###End Bar Graph Example###