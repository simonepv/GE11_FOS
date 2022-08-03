import os
import sys
import ROOT
import array

ROOT.gROOT.SetBatch(True)

def main():
    inFileListName = "ListDataFile.txt"
    inFileListHandle = open( inFileListName, 'r' )
    outDir = "Plots"
    os.system( "mkdir "+outDir )
    outFileName = outDir+"/plot.root"
    outFileHandle = ROOT.TFile.Open(outFileName ,"RECREATE")
    for line in inFileListHandle:
        dataFileName = line[:-1]
        dataFileHandle = open( dataFileName, 'r' )
        timeList = []
        valList  = []
        for lineData in dataFileHandle:
            lineDataSplit = lineData.split('\t')
            timeList.append(float(lineDataSplit[0])) 
            valList.append(float(lineDataSplit[1])) 
        dataFileHandle.close()
        #create the plot
        if len(valList) != 0:
           tg1 = ROOT.TGraph( len(valList), array.array('d',timeList), array.array('d',valList) )
        else: 
           tg1 = ROOT.TGraph()
        #
        #Find name of the sensor
        sensorSplit = dataFileName.split("_")
        sensorName = "FOS_"+sensorSplit[1]+"_"+sensorSplit[2]
        #
        tg1.SetNameTitle( sensorName, sensorName )
        tg1.SetMarkerColor( 1 )
        tg1.SetLineColor( 1 )
        tg1.SetMarkerSize( 1 )
        tg1.SetMarkerStyle( 20 )
        tg1.GetXaxis().SetTimeDisplay(1);
        tg1.GetXaxis().SetTimeFormat("%Y-%m-%d %H:%M");
        tg1.GetXaxis().SetTimeOffset(0,"gmt");
        tg1.GetXaxis().SetTitle("Date (YYYY-MM-DD HH24:MM:SS)")
        tg1.GetYaxis().SetTitle("Not calibrated FOS temperature (Celsius degrees)")
        tg1.Write()
    outFileHandle.Close()
    inFileListHandle.close()




if __name__ == '__main__':
   main()
