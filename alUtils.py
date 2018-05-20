import sqlite3 as sql

OBJ_FIELD_LIST=["PREFIX TEXT","OBJECT TEXT","OTHER TEXT","TYPE TEXT","CON TEXT","RA TEXT","DEC TEXT","MAG REAL","SUBR TEXT",
                "U2K TEXT","TI TEXT","SIZE_MAX TEXT","SIZE_MIN TEXT","PA TEXT",
                "CLASS TEXT","NSTS TEXT","BRSTR TEXT","BCHM TEXT","NGC_DESCR TEXT","NOTES TEXT"]

OBJ_FIELD_NAME=["PREFIX","OBJECT","OTHER","TYPE","CON","RA","DEC","MAG REAL","SUBR",
                "U2K","TI","SIZE_MAX","SIZE_MIN","PA",
                "CLASS","NSTS","BRSTR","BCHM","NGC_DESCR","NOTES"]


AL_DB='./astroListDB.sqlite'

dbConn=None

def createObjTableFromCSV(sourceFile='/Users/rich/Documents/Astronomy/lists/SAC_DeepSky_ver81/SAC_DeepSky_Ver81_QCQ_trimmed.TXT', targetFile=AL_DB, tableName='OBJECTS'):
    """
    Creates an object table of a source CSV file.  By default, uses SAC format
    :param sourceFile: Object list to load
    :param targetFile: databaseFile to add table to
    :return:
    """


    conn=sql.connect(targetFile)
    c=conn.cursor()

    #Create the table
    fieldList=','.join(OBJ_FIELD_LIST)
    sqlC="DROP TABLE {0}".format(tableName)
    c.execute(sqlC)
    conn.commit()

    sqlC = "CREATE TABLE {0} ({1})".format(tableName, fieldList)
    c.execute(sqlC)
    conn.commit()

    i=1
    f=open(sourceFile,'r')
    f.readline() #Skip labels
    for l in f:
        print i
        i+=1
        dataList=l.split(',')

        objNameSplit=dataList[0].split(' ')
        if len(objNameSplit)==1:
            objID=dataList[0]
            objPrefix='"NONE"'
        else:
            objPrefix=objNameSplit[0]+'"'
            objID='"' + ' '.join(objNameSplit[1:])

        dataList[0]=objID
        dataList.insert(0,objPrefix)
        print dataList

        sqlC="INSERT INTO {0} VALUES({1})".format(tableName, ','.join(dataList))
        c.execute(sqlC)
        conn.commit()

    f.close()



    c.execute("CREATE INDEX OBJNAME ON {0} (PREFIX, OBJECT)".format(tableName))
    conn.commit()
    conn.close()


def executeQuery(query):
    """
    Quick utility function to query the DB
    :param query:
    :param limit:
    :return:
    """

    global dbConn
    if not dbConn:
        dbConn = sql.connect(AL_DB)

    c=dbConn.cursor()
    c.execute(query)

    return c.fetchall()
