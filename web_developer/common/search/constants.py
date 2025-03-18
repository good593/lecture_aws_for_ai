import enum 

class TICKER_TYPE(enum.Enum):
    Oil = (enum.auto(), 'CL=F', "석유")
    dollar = (enum.auto(), 'DX-Y.NYB', "달러 인덱스")
    Gold = (enum.auto(), 'GC=F', "금")
    Copper = (enum.auto(), 'HG=F', "구리")
    KOSPI = (enum.auto(), '^KS11', "코스피")



