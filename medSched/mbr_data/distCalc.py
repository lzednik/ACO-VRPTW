import csv

#read zip boundaries
with open('census/zip_bounds.csv', 'r') as f:
  reader = csv.reader(f)
  csv_zip_bounds = list(reader)[1:]


        
#process zip boundaries
zip_bounds={}
for line in csv_zip_bounds:
    zip_cd=line[3]
    
    if len(line[11])>0 and zip_cd in cov_area_zips:
        xml = ET.fromstring(line[11])
        coor_all=[]
        for coord in xml.getiterator('coordinates'):
            coords1=coord.text.split(' ')
            cl2=[]
            for coord1 in coords1:
                coord2=coord1.split(',')
                cl2.append((float(coord2[0]),float(coord2[1])))
                
            coor_all.append(cl2)

        zip_bounds[zip_cd]=coor_all

