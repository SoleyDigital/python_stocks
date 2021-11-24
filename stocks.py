#  VERSION 1
# # DOCN Open
# docn_open = 99.24
# print('$DOCN Open', docn_open)
# # DOCN High Stock 
# docn_high = 104.86
# print('$DOCN High', docn_high)
# # DOCN Low Stock 
# docn_low = 94.74
# print('$DOCN Low', docn_low)
# # DOCN Closed
# docn_closed = 98.96
# print('$DOCN Closed', docn_low)

# VERSION 2
#DigitalOceanHoldings
import yfinance as yf
docn = yf.download("DOCN", period="1d")
print("$DOCN", docn)

#TESLA
tsla = yf.download("TSLA", period="1d")
print( tsla)
