d <- read.table('res.txt')
names(d) <- c('alpha','ss','real','imag')

pdf('rep_bif1.pdf')
plot( d$real, d$imag, type='l', lty=1, lwd=2, cex.lab=1.5, cex.main=1.5, mgp = c(2.3,1,0), xlab="Re(lambda)", ylab="Im(lambda)", ylim=c(-1.7,1.7), main="Evolution of the eigenvalues" )
lines( d$real, -d$imag, type='l', lty=1, lwd=2 )
abline(v=0,col='red')
arrows(0.2,0.0,0.6,0.0, lwd=3)
text(x=0.4, y=0.0, labels=expression(alpha), cex=5, pos=3)
dev.off()

pdf('rep_bif2.pdf')
dstable <- d[ d$real <= 0, ]
dunstable <- d[ d$real > 0, ]

plot( dstable$alpha, dstable$ss, ylim=c(0,5), xlim=c(0,100), type='l', lty=1, lwd=2, cex.lab=1.5, cex.main=1.5, mgp = c(2.3,1,0), xlab=expression(alpha), ylab="steady state", main="Evolution of the steady state" )
lines( dunstable$alpha, dunstable$ss, ylim=c(0,5), lty=2, lwd=2 )
legend("bottomright",legend=c('stable','unstable'),lty=c(1,2), lwd=2)
dev.off()
