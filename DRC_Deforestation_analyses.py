# coding=utf-8
# ============================================================
# Analyzing deforestation around and within PA and LC in DRC
# ============================================================

import arcpy
from arcpy import env
from arcpy.sa import *

print "System modules import successful"

#
# Set environment settings
env.workspace = "H:/Confiance_WRI/COD_Defor/drc.gdb"
outFolder = env.workspace
arcpy.env.overwriteOutput = True
print "Environment set"

# ===============================================================
# Zonal statistics: calculte areas for protected areas
# ===============================================================
## Creating buffers for Protected areas
# Description: Create multiple buffers for the input features

# Set local variables
inFeatures = "cod_atlas_forestier_DBO_aires_protegees_diss"
outFeatureClass = "drc_pa_buffers"
distances = [-10000, 1, 10000]
bufferUnit = "meters"
print "Local variables set"

## Execute MultipleRingBuffer
arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distances, bufferUnit, "", "ALL")
print "Buffer execution successful"

## Execute AddField
# Set local variables
inTable = outFeatureClass
fieldName = "Buff"
fieldLength = 10
arcpy.AddField_management(inTable, fieldName, "TEXT", "", "", fieldLength)
print "Field added for PA Buf"

## Execute CalculateField
expression = "getClass(!distance!)"
codeblock = """def getClass(ring):
    if ring == -10000:
        return 'Core'
    if ring == 1:
        return 'Limit'
    else:
        return 'Buffer'"""
arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON_9.3", codeblock)
print "Field calculations successful for Buffer types"

## Execute Zonal statistics as table for each mask (year)
# Set Mask environment
myfiles = r'H:\Confiance_WRI\COD_Defor\drc.gdb\Newlist.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "drc_pa_buffers"
    InZoneField = "Buff"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStatArea_pa_" + mask
    print OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats Process complete successfully!"

# ===============================================================
# Zonal statistics: calculte areas for logging concessions
# ===============================================================
## Creating buffers for logging concessions
# Description: Create multiple buffers for the input features

# Set local variables
inputFeatures = "cod_atlas_forestier_DBO_ccfs_diss"
outputFeatureClass = "drc_lc_buffers"
bufferUnit = "meters"
print "Local variables set"

# Execute MultipleRingBuffer
arcpy.MultipleRingBuffer_analysis(inputFeatures, outputFeatureClass, distances, bufferUnit, "", "ALL")
print "Buffer execution successful"

## Execute AddField
# Set local variables
inTable1 = outputFeatureClass
arcpy.AddField_management(inTable1, fieldName, "TEXT", "", "", fieldLength)
print "Field added for LC Buf"

## Execute CalculateField
arcpy.CalculateField_management(inTable1, fieldName, expression, "PYTHON_9.3", codeblock)
print "Field calculations successful for Buffer types"

## Execute Zonal stats as table for logging concessions
# Set Mask environment
myfiles = r'H:\Confiance_WRI\COD_Defor\drc.gdb\Newlist.txt'
mymasks = open(myfiles, 'r')
print "Reading raster list successful"

for line in mymasks:
    mask = line.strip('\n')

    arcpy.env.mask = mask
    # Set local variables
    InZones = "drc_lc_buffers"
    InZoneField = "Buff"
    InValueRaster = "Hansen_2013_area_drc"
    OutTable = "ZonStat_Area_lc_" + mask
    print OutTable
    print "Mask Environment set"

    # Check out ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    print "Spatial analyst extension checked!"

    # Execute ZonalStatistics
    outputZStat = ZonalStatisticsAsTable(InZones, InZoneField, InValueRaster, OutTable, "DATA", "SUM")
    print "Zonal stats successful for " + mask

print "Zonal stats Process complete successfully!"
