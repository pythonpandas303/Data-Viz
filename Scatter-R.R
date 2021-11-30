plot(mass~fl,data=BullTroutRML1,ylim=c(0,1600),xlim=c(0,500),  
ylab="Weight (g)",xlab="Fork Length (mm)",  
pch=19,col=rgb(0,0,0,1/4)) 

legend("topleft",inset=0.05,legend=levels(BullTroutRML1$era),  
pch=pchs,col=cols,bty="n",cex=0.75) 