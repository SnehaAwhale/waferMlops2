# import re
#
# regex = "['wafer']|['Wafer']+['\_'']+[\d_]+[\d]+\.csv"
#
# filename='wafer_12_20012.csv'
#
# print(re.match(regex,filename))
# file = open("Training_Logs/GeneralLog.txt", 'a+')

from Training_Raw_Data_Validation.rawValidation import Raw_Data_Validation

Raw_Data_Validation1=Raw_Data_Validation('Training_Batch_Files')
# Raw_Data_Validation1.validationFileNameRaw()


# Raw_Data_Validation1.deleteExistingBadDataTrainingFolder()
# Raw_Data_Validation1.deleteExistingGoodDataTrainingFolder()
# Raw_Data_Validation1.createDirectoryForGoodBadRawData()
# regex=Raw_Data_Validation1.manualRegexCreation()
# values=Raw_Data_Validation1.valuesFromSchema()
# LengthOfDateStampInFile=values[0]
# LengthOfTimeStampInFile=values[1]
# NumberofColumns=values[3]
# Raw_Data_Validation1.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
# # Raw_Data_Validation1.validationFileNameRaw()
# Raw_Data_Validation1.validateColumnLength(NumberofColumns)
# Raw_Data_Validation1.validateMissingValuesInWholeColumn()



