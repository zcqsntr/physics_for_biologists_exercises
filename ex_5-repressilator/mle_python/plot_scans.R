
pdf('single_scans.pdf')
for(i in c('alpha0','n','beta','alpha','var')){
  f <-  paste("single_scan_",i,".txt",sep='')
  d <- read.table(f)
  plot(d[,1],d[,2], main="", xlab=i, ylab=expression(lnl(theta)), cex.lab=1.5, font.axis = 4, mgp = c(2.3,1,0), type='l' )
}
dev.off()
