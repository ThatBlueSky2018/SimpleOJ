import pymysql
import time
import os
import filecmp
import subprocess as sp
import json 
import zipfile
import shutil

def un_zip(file_name,name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)

    for names in zip_file.namelist():
        zip_file.extract(names,"code/data/"+name)
    zip_file.close()

while(True):
        
        db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='oj')
 
        cursor = db.cursor()

        sql = "select  code from judgeStatus_judgestatus where result = -1   limit 1  ";
        cursor.execute(sql)
        code = cursor.fetchall()
        if(code==()):
          time.sleep(0.5)
          continue
        sql = "select  id from judgeStatus_judgestatus where result = -1  limit 1  ";
        cursor.execute(sql)
        id = cursor.fetchall()
         
        sql = "select  problemID_id from judgeStatus_judgestatus where result = -1  limit 1  ";
        cursor.execute(sql)
        p_id = cursor.fetchall()[0][0]
        print(p_id)
        
    
                
        sql = "update judgeStatus_judgestatus set result = -2 where id = %d"% (id[0]);
        cursor.execute(sql)
        db.commit()
        print(code[0][0])
        f = open("code/a.cpp","w")
        f.write(code[0][0])
        f.close()
        Complie_St=os.system("g++  -Wall -O2 -std=c++14  code/a.cpp -o code/a.out  ")
        max_memoryCost=0
        max_cpuTimeCost=0
        fin_condition=-5
        Status=-5
        num=10
        
        print(Complie_St)
        if (Complie_St == 256 ):
            Status=-4
            num=0
            
        un_zip("code/data/%s.zip"%p_id,p_id)
        for i in range(num):
                test_in="test"+str(i)
                test_out="test"+str(i)
                std_out="std"+str(i)
                print("build/y_judge -r ./code/a.out \
                     -i ./code/data/%s/%s.in \
                    -o ./code/data/%s/%s.out -t 1000 -g 1"%(p_id,test_out,p_id,test_out))
                result=sp.Popen("build/y_judge -r ./code/a.out \
                     -i ./code/data/%s/%s.in \
                    -o ./code/data/%s/%s.out -t 1000 -g 1"%(p_id,test_out,p_id,test_out),shell=True,stdout=sp.PIPE)
                out,err = result.communicate() 
                print(out,err)
                print("./code/data/"+p_id+'/'+test_out+".out")
                print("./code/data/"+p_id+'/'+std_out+".out")
      
                #print(out)
                f = open("code/info.json","wb+")
                f.write(out)
                f.close()
                  
                f = open("code/info.json","r")
                Json = f.read()
                f.close()
                    
                Judge_info = json.loads(Json)
                #print(Judge_info)
                memoryCost = Judge_info.get('memoryCost')
                cpuTimeCost = Judge_info['cpuTimeCost']
                condition = Judge_info['condition']
                if(condition != 1):
                    fin_condition = condition
                print(condition)
                print(memoryCost,cpuTimeCost)
                max_memoryCost=max(max_memoryCost,memoryCost)
                max_cpuTimeCost=max(max_cpuTimeCost,cpuTimeCost)
                if(fin_condition == 3):
                    Status = 2
                    break
                if(fin_condition == 4):
                    Status = 3
                    break
                status = filecmp.cmp("./code/data/"+p_id+'/'+test_out+".out","./code/data/"+p_id+'/'+ std_out+".out")
                if status:
                        print("Accept!" ,i)
                else:
                        print("Wrong!" ,i)
                        Status = -3
                        break
                time.sleep(0.5)
                
                
        if(fin_condition == 2):
            Status = 4       
        if(fin_condition == 6):
            Status = 4

        sql = "update judgeStatus_judgestatus set result = %d where id = %d"%(Status,id[0][0]);
        cursor.execute(sql)
        
        #print(max_memoryCost,max_cpuTimeCost)
        sql = "update judgeStatus_judgestatus set memory = %d where id = %d" % (int(max_memoryCost),id[0][0]);
        #print(sql)
        cursor.execute(sql)
        
        sql = "update judgeStatus_judgestatus set time = %d where id = %d"%(max_cpuTimeCost,id[0][0]);
        cursor.execute(sql)
        db.commit()
        cursor.close()
        shutil.rmtree("./code/data/"+p_id)
