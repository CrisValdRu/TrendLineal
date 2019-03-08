import sys
import rrdtool
import time
ultima_lectura = int(rrdtool.last("trafico.rrd"))
tiempo_final = ultima_lectura
tiempo_inicial = tiempo_final - 3600

ret = rrdtool.graphv( "deteccion.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Bytes/s",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                     "DEF:cargaCPU=trend.rrd:CPUload:AVERAGE",

                     "CDEF:umbral25=cargaCPU,25,LT,0,carga,IF",
                     "VDEF:cargaMAX=carga,MAXIMUM",
                     "VDEF:cargaMIN=carga,MINIMUM",
                     "VDEF:cargaSTDEV=carga,STDEV",
                     "VDEF:cargaLAST=carga,LAST",
                     "AREA:carga#00FF00:Carga del CPU",
                     "AREA:carga25#FF9F00:Tráfico de carga mayor que 25",
                     "HRULE:25#FF0000:Umbral 1 - 25%",
                     "PRINT:cargaMAX:%6.2lf %SMAX",
                     "GPRINT:cargaMIN:%6.2lf %SMIN",
                     "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )
print (ret)
print(ret.keys())
print(ret.items())